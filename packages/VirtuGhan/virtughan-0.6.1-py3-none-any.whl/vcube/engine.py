import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import rasterio
from PIL import Image
from pyproj import Transformer
from rasterio.windows import from_bounds

# from scipy.stats import mode
from tqdm import tqdm

from .utils import (
    filter_intersected_features,
    remove_overlapping_sentinel2_tiles,
    search_stac_api,
    smart_filter_images,
    zip_files,
)

matplotlib.use("Agg")


class VCubeProcessor:
    def __init__(
        self,
        bbox,
        start_date,
        end_date,
        cloud_cover,
        formula,
        band1,
        band2,
        operation,
        timeseries,
        output_dir,
        log_file=sys.stdout,
        cmap="RdYlGn",
        workers=1,
        smart_filter=True,
    ):
        self.bbox = bbox
        self.start_date = start_date
        self.end_date = end_date
        self.cloud_cover = cloud_cover
        self.formula = formula or "band1"
        self.band1 = band1
        self.band2 = band2
        self.operation = operation
        self.timeseries = timeseries
        self.output_dir = output_dir
        self.log_file = log_file
        self.cmap = cmap
        self.workers = workers
        self.result_list = []
        self.dates = []
        self.crs = None
        self.transform = None
        self.intermediate_images = []
        self.intermediate_images_with_text = []
        self.use_smart_filter = smart_filter

    def fetch_process_custom_band(self, band1_url, band2_url):
        """Fetch and process custom band data."""
        try:
            with rasterio.open(band1_url) as band1_cog:
                min_x, min_y, max_x, max_y = self._transform_bbox(band1_cog.crs)
                band1_window = self._calculate_window(
                    band1_cog, min_x, min_y, max_x, max_y
                )

                if self._is_window_out_of_bounds(band1_window):
                    return None, None, None

                band1 = band1_cog.read(window=band1_window).astype(float)

                if band2_url:
                    with rasterio.open(band2_url) as band2_cog:
                        min_x, min_y, max_x, max_y = self._transform_bbox(band2_cog.crs)
                        band2_window = self._calculate_window(
                            band2_cog, min_x, min_y, max_x, max_y
                        )

                        if self._is_window_out_of_bounds(band2_window):
                            return None, None, None

                        band2 = band2_cog.read(window=band2_window).astype(float)
                        result = eval(self.formula)
                else:
                    result = eval(self.formula) if band1.shape[0] == 1 else band1

            return (
                result,
                band1_cog.crs,
                band1_cog.window_transform(band1_window),
                band1_url,
            )
        except Exception as e:
            print(f"Error fetching image: {e}")
            return None, None, None

    def _remove_overlapping_sentinel2_tiles(self, features):
        zone_counts = {}
        # lets see how many zones we have in total images
        for feature in features:
            zone = feature["id"].split("_")[1][:2]
            zone_counts[zone] = zone_counts.get(zone, 0) + 1
        # lets get the maximum occorance zone so that when we remove duplicates later on we atleast will try to keep the same zone tiles
        max_zone = max(zone_counts, key=zone_counts.get)

        filtered_features = {}
        for feature in features:
            parts = feature["id"].split("_")
            date = parts[2]
            zone = parts[1][:2]

            # if the zone is the most occuring zone then we will keep it but making sure that same date image is not present in the filtered list
            if zone == max_zone and date not in filtered_features:
                filtered_features[date] = feature

        return list(filtered_features.values())

    def _transform_bbox(self, crs):
        transformer = Transformer.from_crs("epsg:4326", crs, always_xy=True)
        min_x, min_y = transformer.transform(self.bbox[0], self.bbox[1])
        max_x, max_y = transformer.transform(self.bbox[2], self.bbox[3])
        return min_x, min_y, max_x, max_y

    def _calculate_window(self, cog, min_x, min_y, max_x, max_y):
        return from_bounds(min_x, min_y, max_x, max_y, cog.transform)

    def _is_window_out_of_bounds(self, window):
        return (
            window.col_off < 0
            or window.row_off < 0
            or window.width <= 0
            or window.height <= 0
        )

    def _get_band_urls(self, features):
        band1_urls = [feature["assets"][self.band1]["href"] for feature in features]
        band2_urls = (
            [feature["assets"][self.band2]["href"] for feature in features]
            if self.band2
            else [None] * len(features)
        )
        return band1_urls, band2_urls

    def _process_images(self):
        features = search_stac_api(
            self.bbox,
            self.start_date,
            self.end_date,
            self.cloud_cover,
        )
        print(f"Total scenes found: {len(features)}")
        filtered_features = filter_intersected_features(features, self.bbox)
        print(f"Scenes covering input area: {len(filtered_features)}")
        overlapping_features_removed = remove_overlapping_sentinel2_tiles(
            filtered_features
        )
        print(f"Scenes after removing overlaps: {len(overlapping_features_removed)}")
        if self.use_smart_filter:
            overlapping_features_removed = smart_filter_images(
                overlapping_features_removed, self.start_date, self.end_date
            )
            print(
                f"Scenes after applying smart filter: {len(overlapping_features_removed)}"
            )

        band1_urls, band2_urls = self._get_band_urls(overlapping_features_removed)

        if self.workers > 1:
            print("Using Parallel Processing...")
            with ThreadPoolExecutor(max_workers=self.workers) as executor:
                futures = [
                    executor.submit(
                        self.fetch_process_custom_band, band1_url, band2_url
                    )
                    for band1_url, band2_url in zip(band1_urls, band2_urls)
                ]
                for future in tqdm(
                    as_completed(futures),
                    total=len(futures),
                    desc="Computing Band Calculation",
                    file=self.log_file,
                ):
                    result, crs, transform, name_url = future.result()
                    if result is not None:
                        self.result_list.append(result)
                        self.crs = crs
                        self.transform = transform
                        parts = name_url.split("/")
                        image_name = parts[
                            -2
                        ]  # fix this for other images than sentinel
                        self.dates.append(image_name.split("_")[2])
                        if self.timeseries:
                            self._save_intermediate_image(result, image_name)
        else:
            for band1_url, band2_url in tqdm(
                zip(band1_urls, band2_urls),
                total=len(band1_urls),
                desc="Computing Band Calculation",
                file=self.log_file,
            ):
                result, self.crs, self.transform, name_url = (
                    self.fetch_process_custom_band(band1_url, band2_url)
                )
                if result is not None:
                    self.result_list.append(result)
                    parts = name_url.split("/")
                    image_name = parts[-2]
                    self.dates.append(image_name.split("_")[2])

                    if self.timeseries:
                        self._save_intermediate_image(result, image_name)

    def _save_intermediate_image(self, result, image_name):

        output_file = os.path.join(self.output_dir, f"{image_name}_result.tif")
        self._save_geotiff(result, output_file)
        self.intermediate_images.append(output_file)
        self.intermediate_images_with_text.append(
            self.add_text_to_image(output_file, image_name)
        )

    def _save_geotiff(self, data, output_file):
        nodata_value = -9999
        data = np.where(np.isnan(data), nodata_value, data)

        with rasterio.open(
            output_file,
            "w",
            driver="GTiff",
            height=data.shape[1],
            width=data.shape[2],
            count=data.shape[0],
            dtype=data.dtype,
            crs=self.crs,
            transform=self.transform,
            nodata=nodata_value,
        ) as dst:
            for band in range(1, data.shape[0] + 1):
                dst.write(data[band - 1], band)

    def _aggregate_results(self):

        sorted_dates_and_results = sorted(
            zip(self.dates, self.result_list), key=lambda x: x[0]
        )
        sorted_dates, sorted_results = zip(*sorted_dates_and_results)

        max_shape = tuple(max(s) for s in zip(*[arr.shape for arr in sorted_results]))
        padded_result_list = [self._pad_array(arr, max_shape) for arr in sorted_results]
        result_stack = np.ma.stack(padded_result_list)

        operations = {
            "mean": np.ma.mean,
            "median": np.ma.median,
            "max": np.ma.max,
            "min": np.ma.min,
            "std": np.ma.std,
            "sum": np.ma.sum,
            "var": np.ma.var,
        }

        aggregated_result = operations[self.operation](result_stack, axis=0)

        dates = sorted_dates
        dates_numeric = np.arange(len(dates))

        values_per_date = operations[self.operation](result_stack, axis=(1, 2, 3))

        slope, intercept = np.polyfit(dates_numeric, values_per_date, 1)
        trend_line = slope * dates_numeric + intercept

        plt.figure(figsize=(10, 5))
        plt.plot(
            dates,
            values_per_date,
            marker="o",
            linestyle="-",
            label=f"{self.operation.capitalize()} Value",
        )
        plt.plot(dates, trend_line, color="red", linestyle="--", label="Trend Line")
        plt.xlabel("Date")
        plt.ylabel(f"{self.operation.capitalize()} Value")
        plt.title(f"{self.operation.capitalize()} Value Over Time")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()

        plt.savefig(os.path.join(self.output_dir, "values_over_time.png"))
        plt.close()

        return aggregated_result

    def save_aggregated_result_with_colormap(self, result_aggregate, output_file):
        result_aggregate = np.ma.masked_invalid(result_aggregate)
        image = self._create_image(result_aggregate)
        self._plot_result(image, output_file)
        self._save_geotiff(result_aggregate, output_file)

    def _create_image(self, data):
        if data.shape[0] == 1:
            result_normalized = (data[0] - data[0].min()) / (
                data[0].max() - data[0].min()
            )
            colormap = plt.get_cmap(self.cmap)
            result_colored = colormap(result_normalized)
            return (result_colored[:, :, :3] * 255).astype(np.uint8)
        else:
            image_array = np.transpose(data, (1, 2, 0))
            image_array = (
                (image_array - image_array.min())
                / (image_array.max() - image_array.min())
                * 255
            )
            return image_array.astype(np.uint8)

    def _plot_result(self, image, output_file):
        plt.figure(figsize=(10, 10))
        plt.imshow(image)
        plt.title(f"Aggregated {self.operation} Calculation")
        plt.xlabel(
            f"From {self.start_date} to {self.end_date}\nCloud Cover < {self.cloud_cover}%\nBBox: {self.bbox}\nTotal Scene Processed: {len(self.result_list)}"
        )
        plt.colorbar(
            plt.cm.ScalarMappable(
                cmap=plt.get_cmap(self.cmap),
            ),
            ax=plt.gca(),
            shrink=0.5,
        )
        plt.savefig(
            output_file.replace(".tif", "_colormap.png"),
            bbox_inches="tight",
            pad_inches=0.1,
        )
        plt.close()

    def _pad_array(self, array, target_shape, fill_value=np.nan):
        pad_width = [
            (0, max(0, target - current))
            for current, target in zip(array.shape, target_shape)
        ]
        return np.pad(array, pad_width, mode="constant", constant_values=fill_value)

    def add_text_to_image(self, image_path, text):
        with rasterio.open(image_path) as src:
            image_array = (
                src.read(1)
                if src.count == 1
                else np.dstack([src.read(i) for i in range(1, 4)])
            )
            image_array = (
                (image_array - image_array.min())
                / (image_array.max() - image_array.min())
                * 255
            )
            image = Image.fromarray(image_array.astype(np.uint8))

        plt.figure(figsize=(10, 10))
        plt.imshow(image, cmap=self.cmap if src.count == 1 else None)
        plt.axis("off")
        plt.title(text)
        temp_image_path = os.path.splitext(image_path)[0] + "_text.png"
        plt.savefig(temp_image_path, bbox_inches="tight", pad_inches=0.1)
        plt.close()
        return temp_image_path

    @staticmethod
    def create_gif(image_list, output_path, duration_per_image=1):
        sorted_image_list = sorted(image_list)

        images = [Image.open(image_path) for image_path in sorted_image_list]
        max_width = max(image.width for image in images)
        max_height = max(image.height for image in images)
        resized_images = [
            image.resize((max_width, max_height), Image.LANCZOS) for image in images
        ]

        frame_duration = duration_per_image * 1000

        resized_images[0].save(
            output_path,
            save_all=True,
            append_images=resized_images[1:],
            duration=frame_duration,
            loop=0,
        )
        print(f"Saved timeseries GIF to {output_path}")

    def compute(self):
        print("Engine starting...")
        os.makedirs(self.output_dir, exist_ok=True)
        if not self.band1:
            raise Exception("Band1 is required")

        print("Searching STAC .....")
        self._process_images()

        if self.result_list and self.operation:
            print("Aggregating results...")
            result_aggregate = self._aggregate_results()
            output_file = os.path.join(
                self.output_dir, "custom_band_output_aggregate.tif"
            )
            print("Saving aggregated result with colormap...")
            self.save_aggregated_result_with_colormap(result_aggregate, output_file)

        if self.timeseries:
            print("Creating GIF and zipping TIFF files...")
            if self.intermediate_images:
                self.create_gif(
                    self.intermediate_images_with_text,
                    os.path.join(self.output_dir, "output.gif"),
                )
                zip_files(
                    self.intermediate_images,
                    os.path.join(self.output_dir, "tiff_files.zip"),
                )
            else:
                print("No images found for the given parameters")


if __name__ == "__main__":
    # Example usage
    bbox = [83.84765625, 28.22697003891833, 83.935546875, 28.304380682962773]
    start_date = "2024-12-15"
    end_date = "2024-12-31"
    cloud_cover = 30
    formula = "(band2-band1)/(band2+band1)"  # NDVI formula
    band1 = "red"
    band2 = "nir"
    operation = "median"
    timeseries = True
    output_dir = "./output"
    workers = 1  # Number of parallel workers
    os.makedirs(output_dir, exist_ok=True)

    processor = VCubeProcessor(
        bbox,
        start_date,
        end_date,
        cloud_cover,
        formula,
        band1,
        band2,
        operation,
        timeseries,
        output_dir,
        workers=workers,
    )
    processor.compute()
