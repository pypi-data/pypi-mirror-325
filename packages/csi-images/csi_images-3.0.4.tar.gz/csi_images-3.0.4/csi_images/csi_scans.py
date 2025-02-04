"""
Contains the Scan class, which holds important metadata from a scan. This metadata
can be exported to a .yaml file, which can be loaded back into a Scan object. The Scan
object can also be loaded from a .czi file or a .txt file.
"""

import os
import math
import enum
import datetime
import zoneinfo
from typing import Self, Iterable

import yaml
import json

try:
    import aicspylibczi
except ImportError:
    aicspylibczi = None


class Scan(yaml.YAMLObject):
    """
    Class that composes a whole scan's metadata. Contains some universal data,
    plus lists for channels and ROIs.

    .. include:: ../docs/coordinate_systems.md
    """

    yaml_tag = "csi_images.csi_scans.Scan"

    class Type(enum.Enum):
        BZSCANNER = "bzscanner"
        AXIOSCAN7 = "axioscan7"

    SCANNER_IDS = {"4661000426": f"{Type.AXIOSCAN7.value}_0"}
    """Axioscan 7 scanner IDs (service number), mapped to our scanner IDs"""

    METADATA_FILE_NAME = {
        Type.AXIOSCAN7: "scan.yaml",
        Type.BZSCANNER: "slideinfo.txt",
    }
    STANDARD_DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S%z"
    DATETIME_FORMAT = {
        Type.AXIOSCAN7: STANDARD_DATETIME_FORMAT,
        Type.BZSCANNER: "%a %b %d %H:%M:%S %Y",
    }

    # Actual channel names, from the BZScanner's default order
    BZSCANNER_CHANNEL_MAP = {
        "DAPI": "DAPI",
        "TRITC": "AF555",
        "CY5": "AF647",
        "BF": "BRIGHT",
        "FITC": "AF488",
    }

    class Channel(yaml.YAMLObject):
        """
        Class that comprises a channel; we usually have multiple (2-5) per scan.
        Contains three fields:
        - name: the name of the channel (e.g. DAPI, AF647, AF555, AF488, BRIGHTFIELD)
        - exposure_ms: the exposure time to capture a frame in milliseconds
        - intensity: the light intensity used OR the gain applied to the channel
        """

        yaml_tag = "csi_images.csi_scans.Scan.Channel"

        def __init__(
            self,
            name: str = "",
            exposure_ms: float = -1.0,
            intensity: float = -1.0,
            gain_applied: bool = True,
        ):
            self.name = name
            self.exposure_ms = exposure_ms
            self.intensity = intensity
            self.gain_applied = gain_applied

        def __repr__(self):
            return yaml.dump(self, sort_keys=False)

        def __eq__(self, other):
            return self.__repr__() == other.__repr__()

    class ROI(yaml.YAMLObject):
        """
        Class that comprises an ROI; we usually have 1, but may have more in a scan.
        """

        yaml_tag = "csi_images.csi_scans.Scan.ROI"

        def __init__(
            self,
            origin_x_um: int = -1,
            origin_y_um: int = -1,
            width_um: int = -1,
            height_um: int = -1,
            tile_rows: int = -1,
            tile_cols: int = -1,
            focus_points=None,
        ):
            if focus_points is None:
                focus_points = []
            self.origin_x_um = origin_x_um
            self.origin_y_um = origin_y_um
            self.width_um = width_um
            self.height_um = height_um
            self.tile_rows = tile_rows
            self.tile_cols = tile_cols
            self.focus_points = focus_points

        def __repr__(self):
            return yaml.dump(self, sort_keys=False)

        def __eq__(self, other):
            return self.__repr__() == other.__repr__()

        def similar(self, other):
            return (
                self.origin_y_um == other.origin_y_um
                and self.origin_x_um == other.origin_x_um
                and self.width_um == other.width_um
                and self.height_um == other.height_um
                and self.tile_rows == other.tile_rows
                and self.tile_cols == other.tile_cols
            )

    def __init__(
        self,
        slide_id: str = "",
        scanner_id: str = "",
        path: str = "",
        exists: bool = True,
        start_datetime: str = "",
        end_datetime: str = "",
        scan_time_s: int = -1,
        tray_pos: int = -1,
        slide_pos: int = -1,
        camera: str = "",
        objective: str = "",
        pixel_size_um: float = -1.0,
        tile_width_px: int = -1,
        tile_height_px: int = -1,
        tile_x_offset_px: int = -1,
        tile_y_offset_px: int = -1,
        tile_overlap_proportion: int = -1,
        channels: list[Channel] = None,
        roi: list[ROI] = None,
    ):
        if roi is None:
            roi = []
        if channels is None:
            channels = []
        self.slide_id = slide_id
        self.scanner_id = scanner_id
        self.path = path
        self.exists = exists
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.scan_time_s = scan_time_s
        self.tray_pos = tray_pos
        self.slide_pos = slide_pos
        self.camera = camera
        self.objective = objective
        self.pixel_size_um = pixel_size_um
        self.tile_width_px = tile_width_px
        self.tile_height_px = tile_height_px
        self.tile_x_offset_px = tile_x_offset_px
        self.tile_y_offset_px = tile_y_offset_px
        self.tile_overlap_proportion = tile_overlap_proportion
        self.channels = channels
        self.roi = roi

    def __key(self):
        return (
            self.slide_id,
            self.scanner_id,
            self.path,
            self.exists,
            self.start_datetime,
            self.end_datetime,
            self.scan_time_s,
            self.tray_pos,
            self.slide_pos,
            self.camera,
            self.objective,
            self.pixel_size_um,
            self.tile_width_px,
            self.tile_height_px,
            self.tile_overlap_proportion,
            tuple(self.channels),
            tuple(self.roi),
        )

    def __hash__(self):
        return hash(self.__key())

    def __repr__(self):
        return yaml.dump(self, sort_keys=False)

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

    def has_same_profile(self, other):
        return (
            self.camera == other.camera
            and self.objective == other.objective
            and self.pixel_size_um == other.pixel_size_um
            and self.tile_width_px == other.tile_width_px
            and self.tile_height_px == other.tile_height_px
            and self.tile_x_offset_px == other.tile_x_offset_px
            and self.tile_y_offset_px == other.tile_y_offset_px
            and self.tile_overlap_proportion == other.tile_overlap_proportion
            and self.channels == other.channels
            and all(a.similar(b) for a, b in zip(self.roi, other.roi))
        )

    def get_channel_names(self) -> list[str]:
        """
        Get the channel names in the scan's channel order.
        :return: a list of channel names.
        """
        return [channel.name for channel in self.channels]

    def get_channel_indices(self, channel_names: Iterable[str | None]) -> list[int]:
        """
        Given a list of channel names, return the corresponding indices in the scan's
        channel order. Will convert BZScanner channel names (TRITC, CY5, FITC) to the
        actual AlexaFluor names (AF555, AF647, AF488).
        If a list entry is not found or None, it will return -1 for that entry.
        :param channel_names: a list of channel names.
        :return: a list of channel indices.
        """
        # Get the scan's channel name list
        scan_channel_names = self.get_channel_names()

        channel_indices = []
        for name in channel_names:
            # Convert any BZScanner channel names to the actual channel names
            if name in self.BZSCANNER_CHANNEL_MAP:
                name = self.BZSCANNER_CHANNEL_MAP[name]

            # Append the corresponding index if possible
            if name in scan_channel_names:
                channel_indices.append(scan_channel_names.index(name))
            else:
                channel_indices.append(-1)
        return channel_indices

    def get_image_size(self) -> tuple[int, int]:
        """
        Get the real size of the image in pixels after subtracting overlap.
        :return: a tuple of (real_height, real_width) for easy comparison to arrays
        """
        width_overlap = math.floor(self.tile_width_px * self.tile_overlap_proportion)
        height_overlap = math.floor(self.tile_height_px * self.tile_overlap_proportion)
        return self.tile_height_px - height_overlap, self.tile_width_px - width_overlap

    def save_yaml(self, output_path: str):
        """
        Write the Scan object to a .yaml file.
        :param output_path: /path/to/file.yaml or /path/to/folder to put scan.yaml
        :return: nothing; will raise an error on failure
        """
        # Create necessary folders
        output_path = os.path.abspath(output_path)
        if os.path.splitext(output_path)[1] == ".yaml":
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
        else:
            os.makedirs(output_path, exist_ok=True)
            # Add the standard metadata file name to the path if needed
            output_path = os.path.join(
                output_path, self.METADATA_FILE_NAME[self.Type.AXIOSCAN7]
            )

        # Populate the file
        with open(output_path, "w") as file:
            yaml.dump(self, stream=file, sort_keys=False)

    @classmethod
    def load_yaml(cls, input_path: str) -> Self:
        """
        Load a Scan object from a .yaml file.
        :param input_path: /path/to/file.yaml or /path/to/folder with scan.yaml
        :return: a Scan object
        """
        input_path = os.path.abspath(input_path)
        if os.path.isdir(input_path):
            input_path = os.path.join(
                input_path, cls.METADATA_FILE_NAME[cls.Type.AXIOSCAN7]
            )
        with open(input_path, "r") as file:
            metadata_obj = yaml.load(file, Loader=yaml.Loader)
        return metadata_obj

    def to_dict(self) -> dict:
        """
        Convert the Scan object to a dictionary with keys matching database columns
        and values matching database entries
        :return: a dictionary
        """
        # Dump to json; then add indents and a top-level key
        channels_json = json.dumps(
            self.channels, default=lambda x: x.__dict__, indent=2
        )
        channels_json = "  ".join(channels_json.splitlines(True))
        channels_json = "{\n  " + '"data": ' + channels_json + "\n}"

        roi_json = json.dumps(self.roi, default=lambda x: x.__dict__, indent=2)
        roi_json = "  ".join(roi_json.splitlines(True))
        roi_json = "{\n  " + '"data": ' + roi_json + "\n}"

        # Keys are named the same as database columns
        return {
            "scanner_id": self.scanner_id,
            "slide_id": self.slide_id,
            "exists": self.exists,
            "path": self.path,
            "start_datetime": self.start_datetime,
            "end_datetime": self.end_datetime,
            "scan_time_s": self.scan_time_s,
            "tray_pos": self.tray_pos,
            "slide_pos": self.slide_pos,
            "tile_width": self.tile_width_px,
            "tile_height": self.tile_height_px,
            "tile_x_offset": self.tile_x_offset_px,
            "tile_y_offset": self.tile_y_offset_px,
            "tile_overlap": self.tile_overlap_proportion,
            "camera": self.camera,
            "objective": self.objective,
            "pixel_size": self.pixel_size_um,
            "channels": channels_json,
            "roi": roi_json,
        }

    @classmethod
    def from_dict(cls, scan_dict) -> Self:
        """
        Convert a dictionary from to_dict() or the database to a Scan object
        :param scan_dict: a dictionary
        :return: a Scan object
        """
        result = cls(
            scanner_id=scan_dict["scanner_id"],
            slide_id=scan_dict["slide_id"],
            path=scan_dict["path"],
            exists=scan_dict["exists"],
            start_datetime=scan_dict["start_datetime"],
            end_datetime=scan_dict["end_datetime"],
            scan_time_s=scan_dict["scan_time_s"],
            tray_pos=scan_dict["tray_pos"],
            slide_pos=scan_dict["slide_pos"],
            camera=scan_dict["camera"],
            objective=scan_dict["objective"],
            pixel_size_um=scan_dict["pixel_size"],
            tile_width_px=scan_dict["tile_width"],
            tile_height_px=scan_dict["tile_height"],
            tile_x_offset_px=scan_dict["tile_x_offset"],
            tile_y_offset_px=scan_dict["tile_y_offset"],
            tile_overlap_proportion=scan_dict["tile_overlap"],
        )
        # Handle JSON and dictionaries
        if isinstance(scan_dict["channels"], str):
            channels_dict = json.loads(scan_dict["channels"])["data"]
        else:
            channels_dict = scan_dict["channels"]["data"]
        for channel in channels_dict:
            result.channels.append(
                cls.Channel(
                    name=channel["name"],
                    exposure_ms=channel["exposure_ms"],
                    intensity=channel["intensity"],
                    gain_applied=channel["gain_applied"],
                )
            )
        # Handle JSON and dictionaries
        if isinstance(scan_dict["channels"], str):
            roi_dict = json.loads(scan_dict["roi"])["data"]
        else:
            roi_dict = scan_dict["roi"]["data"]
        for roi in roi_dict:
            result.roi.append(
                cls.ROI(
                    origin_x_um=roi["origin_x_um"],
                    origin_y_um=roi["origin_y_um"],
                    width_um=roi["width_um"],
                    height_um=roi["height_um"],
                    tile_rows=roi["tile_rows"],
                    tile_cols=roi["tile_cols"],
                    focus_points=roi["focus_points"],
                )
            )
        return result

    @classmethod
    def load_czi(cls, input_path: str) -> Self:
        """
        Extracts metadata from a .czi file, which is the output of the Axioscan
        :param input_path: the path to the .czi file
        :return: a Scan object
        """
        if aicspylibczi is None:
            raise ModuleNotFoundError(
                "aicspylibczi library not installed. "
                "Install csi-images with [imageio] option to resolve."
            )

        # Normalize paths
        input_path = os.path.abspath(input_path)

        with open(input_path, "rb") as file:
            # Read in metadata as XML elements
            metadata_xml = aicspylibczi.CziFile(file).meta
            # Read in shape metadata from binary
            rois_shape = aicspylibczi.CziFile(file).get_dims_shape()

        # Populate metadata
        scan = cls()

        scan.slide_id = metadata_xml.find(".//Label/Barcodes/Barcode/Content").text
        if scan.slide_id is not None:
            scan.slide_id = scan.slide_id.strip().upper()
        # Map the raw scanner ID (service ID) to our IDs
        scan.scanner_id = cls.SCANNER_IDS[
            metadata_xml.find(".//Microscope/UserDefinedName").text
        ]

        # Extract start and finish datetimes
        date = metadata_xml.find(".//Document/CreationDate").text
        # Strip out sub-second precision
        date = date[: date.find(".")] + date[max(date.rfind("-"), date.rfind("+")) :]
        date_as_datetime = datetime.datetime.strptime(
            date, cls.DATETIME_FORMAT[cls.Type.AXIOSCAN7]
        )
        scan.start_datetime = date_as_datetime.strftime(cls.STANDARD_DATETIME_FORMAT)
        scan.scan_time_s = round(
            float(metadata_xml.find(".//Image/AcquisitionDuration").text) / 1000
        )
        date_as_datetime += datetime.timedelta(seconds=scan.scan_time_s)
        scan.end_datetime = date_as_datetime.strftime(cls.STANDARD_DATETIME_FORMAT)

        scan.tray_pos = int(metadata_xml.find(".//SlotNumberOfLoadedTray").text)
        scan.slide_pos = int(metadata_xml.find(".//SlideScannerPosition").text[-1])

        # Get camera and magnifying info
        scan.camera = (
            metadata_xml.find(".//Information/Instrument/Detectors/Detector").attrib
        )["Name"]
        magnification = metadata_xml.find(
            ".//Objectives/Objective/NominalMagnification"
        )
        aperture = metadata_xml.find(".//Objectives/Objective/LensNA")
        scan.objective = f"{magnification.text}x-{aperture.text}"
        scan.pixel_size_um = (
            float(metadata_xml.find(".//Scaling/Items/Distance/Value").text) * 1e6
        )
        # Round off the pixel size to nanometers; might not be optimal, but this
        # gets rounded when we send it to the database anyways (to 7 places)
        scan.pixel_size_um = round(scan.pixel_size_um, 3)

        # Get tile information
        # Note: X Y is untested, could be flipped. I always forget. Just don't use
        # non-square frames and we're all good.
        selected_detector = metadata_xml.find(".//SelectedDetector").text
        detectors = metadata_xml.findall(".//Detectors/Detector")
        for detector in detectors:
            if detector.attrib["Id"] == selected_detector:
                tile_info = detector.find(".//Frame")
                break
        # Convert to integers
        tile_info = [int(coordinate) for coordinate in tile_info.text.split(",")]

        scan.tile_x_offset_px = tile_info[0]
        scan.tile_y_offset_px = tile_info[1]
        scan.tile_width_px = tile_info[2]
        scan.tile_height_px = tile_info[3]
        scan.tile_overlap_proportion = float(metadata_xml.find(".//Overlap").text)

        # Extract channels and create Channel objects from them
        channel_indices = []
        for channel in metadata_xml.findall(".//Image/Dimensions/Channels/Channel"):
            channel_indices.append(int(channel.attrib["Id"][-1]))
            intensity_xml = channel.find(".//Intensity")
            if intensity_xml is None:
                intensity = 0
            else:
                intensity = float(intensity_xml.text[:-2]) * 1e-2
            scan.channels.append(
                cls.Channel(
                    name=channel.attrib["Name"].upper(),
                    exposure_ms=float(channel.find("./ExposureTime").text) * 1e-6,
                    intensity=intensity,
                    gain_applied=True,  # In Axioscan, we will always use gain = 1
                )
            )
        # Make sure the channels are sorted
        scan.channels = [
            channel for _, channel in sorted(zip(channel_indices, scan.channels))
        ]
        # Verify that the shape corresponds to the channels
        for roi in rois_shape:
            if roi["C"][1] != len(scan.channels):
                raise ValueError(
                    f"Number of channels {len(scan.channels)} "
                    f"is not the same as the number of channels in an ROI: "
                    f"{roi['C'][1]}"
                )

        # Get the real ROI limits; the metadata is not always correct
        limits_xml = metadata_xml.findall(".//AllowedScanArea")
        limits = [
            round(float(limits_xml[0].find("Center").text.split(",")[0])),
            round(float(limits_xml[0].find("Center").text.split(",")[1])),
            round(float(limits_xml[0].find("Size").text.split(",")[0])),
            round(float(limits_xml[0].find("Size").text.split(",")[1])),
        ]
        # Convert to top-left and bottom-right
        limits = [
            round(limits[0] - limits[2] / 2),
            round(limits[1] - limits[3] / 2),
            round(limits[0] + limits[2] / 2),
            round(limits[1] + limits[3] / 2),
        ]

        # Extract ROIs and create ROI objects from them
        rois_xml_metadata = metadata_xml.findall(".//TileRegions/TileRegion")
        scenes_xml_metadata = metadata_xml.findall(".//S/Scenes/Scene")
        if len(rois_xml_metadata) != len(rois_shape):
            raise ValueError(
                f"Metadata and binary data from {input_path} "
                f"do not match in number of ROIs"
            )
        # We need both to determine the number of rows/columns because the XML lies
        roi_indices = []
        for roi_xml, roi_shape in zip(rois_xml_metadata, rois_shape):
            name = roi_xml.attrib["Name"]
            # Determine the index of this scene
            scene_index = -1
            for scene in scenes_xml_metadata:
                if scene.attrib["Name"] == name:
                    scene_index = int(scene.attrib["Index"])
                    break
            if scene_index == -1:
                raise ValueError(f"ROI {name} does not correspond to any scenes")
            else:
                roi_indices.append(scene_index)
            # Extract other metadata
            roi_limits = [
                round(float(roi_xml.find("CenterPosition").text.split(",")[0])),
                round(float(roi_xml.find("CenterPosition").text.split(",")[1])),
                round(float(roi_xml.find("ContourSize").text.split(",")[0])),
                round(float(roi_xml.find("ContourSize").text.split(",")[1])),
            ]
            # Convert to top-left and bottom-right
            roi_limits = [
                round(roi_limits[0] - roi_limits[2] / 2),
                round(roi_limits[1] - roi_limits[3] / 2),
                round(roi_limits[0] + roi_limits[2] / 2),
                round(roi_limits[1] + roi_limits[3] / 2),
            ]
            # Bound the ROI to the actual scan limits
            roi_limits = [
                max(roi_limits[0], limits[0]),
                max(roi_limits[1], limits[1]),
                min(roi_limits[2], limits[2]),
                min(roi_limits[3], limits[3]),
            ]

            tile_rows = int(roi_xml.find("Rows").text)
            # Current best way of reliably extracting; <Columns> entry can be wrong
            if (roi_shape["M"][1] % tile_rows) != 0:
                raise ValueError(
                    f"The number of tiles {roi_shape['M'][1]} is not "
                    f"divisible by the tile rows {tile_rows}; metadata "
                    f"must be messed up. Thanks Zeiss"
                )
            else:
                tile_cols = int(roi_shape["M"][1] / tile_rows)
            # Support points are actually the relevant focus points for this ROI
            focus_points = []
            for focus_point in roi_xml.findall("SupportPoints/SupportPoint"):
                focus_points.append(
                    [
                        int(float(focus_point.find("X").text)),
                        int(float(focus_point.find("Y").text)),
                        int(float(focus_point.find("Z").text)),
                    ]
                )
            # Strip all sub-micron precision, it does not matter
            scan.roi.append(
                cls.ROI(
                    origin_x_um=roi_limits[0],
                    origin_y_um=roi_limits[1],
                    width_um=roi_limits[2] - roi_limits[0],
                    height_um=roi_limits[3] - roi_limits[1],
                    tile_rows=tile_rows,
                    tile_cols=tile_cols,
                    focus_points=focus_points,
                )
            )
        # Sort based on the scene indices
        scan.roi = [roi for _, roi in sorted(zip(roi_indices, scan.roi))]

        return scan

    @classmethod
    def load_txt(cls, input_path: str) -> Self:
        """
        Loads a Scan object from a .txt file, usually slideinfo.txt, which originates
        from the BZScanner. Some metadata is filled in or adjusted to fit
        :param input_path: /path/to/file.txt or /path/to/folder containing slideinfo.txt
        :return: a Scan object
        """
        # Set paths
        input_path = os.path.abspath(input_path)
        if os.path.isdir(input_path):
            input_path = os.path.join(
                input_path, cls.METADATA_FILE_NAME[cls.Type.BZSCANNER]
            )

        # Read in metadata as a dict
        with open(input_path, "r") as file:
            metadata_contents = file.read()
            # Read each line, splitting on the = sign
            metadata_dict = {}
            for line in metadata_contents.splitlines():
                key, value = line.split("=")
                metadata_dict[key] = value

        # Populate metadata
        scan = cls()

        scan.slide_id = metadata_dict["SLIDEID"]
        scan.slide_id = scan.slide_id.strip().upper()

        scan.path = metadata_dict["SLIDEDIR"]

        # Extract start and finish datetimes
        date = metadata_dict["DATE"]
        date_as_datetime = datetime.datetime.strptime(
            date, cls.DATETIME_FORMAT[cls.Type.BZSCANNER]
        )
        date_as_datetime = date_as_datetime.astimezone(
            zoneinfo.ZoneInfo("America/Los_Angeles")
        )  # Hardcoded because BZScanners are here
        scan.start_datetime = date_as_datetime.strftime(cls.STANDARD_DATETIME_FORMAT)
        scan.scan_time_s = 90 * 60  # estimated 90 minutes per scan
        date_as_datetime += datetime.timedelta(seconds=scan.scan_time_s)
        scan.end_datetime = date_as_datetime.strftime(cls.STANDARD_DATETIME_FORMAT)

        # Map the raw scanner ID (service ID) to our IDs
        scan.scanner_id = f'{cls.Type.BZSCANNER.value}_{metadata_dict["INSTRUMENT"]}'
        scan.tray_pos = 0  # only one tray_pos in a BZScanner
        scan.slide_pos = int(metadata_dict["SLIDEPOS"]) - 1  # 1-indexed

        # Get camera and magnifying info
        scan.camera = ""
        magnification = 10
        aperture = 0  # TODO: find the actual aperture
        scan.objective = f"{magnification}x-{aperture}"
        scan.pixel_size_um = 0.591  # Estimated from image metadata

        # Get tile information
        scan.tile_width_px = 1362  # Known from image metadata
        scan.tile_height_px = 1004  # Known from image metadata
        scan.tile_x_offset_px = 0  # Already removed
        scan.tile_y_offset_px = 0  # Already removed
        scan.tile_overlap_proportion = 0  # Already removed

        # Extract channels and create Channel objects from them
        if "gain_applied" in metadata_dict:
            gain_applied = True if metadata_dict["gain_applied"] == "1" else False
        else:
            gain_applied = True  # Previous policy was always to apply gains
        for channel in list(cls.BZSCANNER_CHANNEL_MAP.keys()):
            channel_settings = metadata_dict[channel].split(",")
            if channel_settings[0] == "0":
                continue
            scan.channels.append(
                cls.Channel(
                    name=cls.BZSCANNER_CHANNEL_MAP[channel],
                    exposure_ms=float(channel_settings[1]),
                    intensity=float(channel_settings[2]),
                    gain_applied=gain_applied,
                )
            )

        # Get focus points
        focus_points = []
        for i in range(33):
            focus_point = metadata_dict["FOCUSPOS" + str(i)].split(",")
            if focus_point[0] == "0":
                break
            focus_points.append(
                [
                    int(float(focus_point[1])),
                    int(float(focus_point[2])),
                    int(float(focus_point[3])),
                ]
            )

        # In the BZScanner, the slide is vertical instead of horizontal
        # We put in nominal values for the ROI, which is oriented vertically as well
        tile_rows = 96
        tile_cols = 24
        roi_width = round(scan.pixel_size_um * scan.tile_width_px * tile_cols)
        roi_height = round(scan.pixel_size_um * scan.tile_height_px * tile_rows)
        origin_x_um = 2500 + round((20000 - roi_width) / 2)
        origin_y_um = 2500 + round((58000 - roi_height) / 2)
        scan.roi.append(
            cls.ROI(
                origin_x_um=origin_x_um,
                origin_y_um=origin_y_um,
                width_um=roi_width,
                height_um=roi_height,
                tile_rows=tile_rows,
                tile_cols=tile_cols,
                focus_points=focus_points,
            )
        )
        return scan

    @classmethod
    def load_from_folder(cls, input_path: str) -> Self:
        """
        Load a Scan object from a folder that contains defaultly-named metadata files,
        scan.yaml or slideinfo.txt. Prefers scan.yaml if both exist
        :param input_path: /path/to/folder
        :return: a Scan object
        """
        input_path = os.path.abspath(input_path)
        if os.path.isfile(
            os.path.join(input_path, cls.METADATA_FILE_NAME[cls.Type.AXIOSCAN7])
        ):
            return cls.load_yaml(input_path)
        elif os.path.isfile(
            os.path.join(input_path, cls.METADATA_FILE_NAME[cls.Type.BZSCANNER])
        ):
            return cls.load_txt(input_path)
        else:
            raise ValueError(
                f"No scan metadata files "
                f"({cls.METADATA_FILE_NAME[cls.Type.AXIOSCAN7]}, "
                f"{cls.METADATA_FILE_NAME[cls.Type.BZSCANNER]}) found in folder "
                f"{input_path}"
            )
        pass

    @classmethod
    def make_placeholder(
        cls,
        slide_id: str,
        n_tile: int = 2303,
        n_roi: int = 0,
        scanner_type: Type = Type.BZSCANNER,
    ) -> Self:
        """
        Make a placeholder Scan object with only basic required information filled in.
        :param slide_id: the slide ID
        :param n_tile: the number of this tile, which will become the number of
                       tiles in the scan
        :param n_roi: the number of ROIs in the scan
        :param scanner_type: the scanner type
        :return: a Scan object
        """
        # Sanitize inputs here
        slide_id = str(slide_id).strip().upper()
        n_tile = int(n_tile)
        n_roi = int(n_roi)
        # Generate the object
        scan = cls()
        scan.slide_id = slide_id
        if scanner_type == cls.Type.AXIOSCAN7:
            scan.scanner_id = f"{cls.Type.AXIOSCAN7.value}_placeholder"
            scan.roi = [cls.ROI() for _ in range(n_roi + 1)]
            scan.roi[0].tile_rows = 17
            scan.roi[0].tile_cols = (n_tile // 17) + 1
            scan.channels = [
                cls.Channel(name="DAPI", exposure_ms=1.0, intensity=1.0),
                cls.Channel(name="AF488", exposure_ms=1.0, intensity=1.0),
                cls.Channel(name="AF555", exposure_ms=1.0, intensity=1.0),
                cls.Channel(name="AF647", exposure_ms=1.0, intensity=1.0),
            ]
        elif scanner_type == cls.Type.BZSCANNER:
            scan.scanner_id = f"{cls.Type.BZSCANNER.value}_placeholder"
            scan.roi = [cls.ROI() for _ in range(n_roi + 1)]
            scan.roi[0].tile_rows = 96
            scan.roi[0].tile_cols = 24
            scan.channels = [
                cls.Channel(name="DAPI", exposure_ms=1.0, intensity=1.0),
                cls.Channel(name="AF555", exposure_ms=1.0, intensity=1.0),
                cls.Channel(name="AF647", exposure_ms=1.0, intensity=1.0),
                cls.Channel(name="AF488", exposure_ms=1.0, intensity=1.0),
            ]
        return scan
