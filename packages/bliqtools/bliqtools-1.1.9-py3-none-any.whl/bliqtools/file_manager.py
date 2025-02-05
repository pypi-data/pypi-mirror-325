import re
from typing import Callable
from enum import Enum, auto
from dataclasses import dataclass
from typing import Optional, List, Dict, Union
import pathlib


@dataclass
class FileFilter:
    """Data class to hold file filtering criteria"""

    extensions: Optional[List[str]] = None
    pattern: Optional[str] = None
    content_check: Optional[Callable[[str], bool]] = None
    description: str = ""


class FileManagerPresetType(Enum):
    """Enum for different preset types"""

    IMAGES = auto()
    DOCUMENTS = auto()
    TIFF = auto()
    TEXT = auto()
    SPREADSHEETS = auto()
    VIDEOS = auto()


def _filter_files(
        root: pathlib.Path,
    files: List[str],
    extensions: Optional[List[str]],
    pattern: Optional[str],
    content_check: Optional[Callable[[pathlib.Path], bool]],
    include_hidden: bool = False,
) -> List[pathlib.Path]:
    """
    Helper method to filter files based on given criteria.

    :param root: Root directory path
    :param files: List of filenames to filter
    :param extensions: List of allowed extensions
    :param pattern: Regex pattern to match
    :param content_check: Content checking function
    :param include_hidden: If True, include hidden files
    :return: List of matching file paths
    """
    matching_files = []

    for filename in files:
        if not include_hidden and filename.startswith("."):
            continue

        filepath = root.joinpath(filename)

        if extensions and not any(
            filename.lower().endswith(ext.lower()) for ext in extensions
        ):
            continue

        if pattern and not re.search(pattern, filename):
            continue

        if content_check and not content_check(filepath):
            continue

        matching_files.append(filepath)

    return matching_files


class FileManager:
    PRESET_FILTERS: Dict[FileManagerPresetType, FileFilter] = {
        FileManagerPresetType.IMAGES: FileFilter(
            extensions=[".jpg", ".jpeg", ".png", ".gif", ".tif", ".tiff", ".bmp"],
            description="Image files",
        ),
        FileManagerPresetType.DOCUMENTS: FileFilter(
            extensions=[".doc", ".docx", ".pdf", ".txt", ".rtf"],
            description="Document files",
        ),
        FileManagerPresetType.TIFF: FileFilter(
            extensions=[".tif", ".tiff"], description="TIFF files"
        ),
        FileManagerPresetType.TEXT: FileFilter(
            extensions=[".txt", ".log", ".csv"], description="Text files"
        ),
        FileManagerPresetType.SPREADSHEETS: FileFilter(
            extensions=[".xls", ".xlsx", ".csv"], description="Spreadsheet files"
        ),
        FileManagerPresetType.VIDEOS: FileFilter(
            extensions=[".mp4", ".avi", ".mov", ".wmv"], description="Video files"
        ),
    }

    def __init__(self, directory: pathlib.Path):
        self.directory = directory
        self.custom_presets: Dict[str, FileFilter] = {}

    def add_custom_preset(self, name: str, file_filter: FileFilter) -> None:
        """Add a custom preset filter"""
        self.custom_presets[name] = file_filter

    def list_files(
        self,
        preset: Optional[Union[FileManagerPresetType, str]] = None,
        extensions: Optional[List[str]] = None,
        pattern: Optional[str] = None,
        content_check: Optional[Callable[[str], bool]] = None,
        recursive: bool = False,
        include_hidden: bool = False,
    ) -> List[pathlib.Path]:
        """
        List files in the directory with optional filtering or using presets.

        :param preset: PresetType enum or custom preset name to use predefined filters
        :param extensions: List of file extensions to include (e.g., ['.tif', '.jpg'])
        :param pattern: Regex pattern to match filenames
        :param content_check: Function that takes a filepath and returns True if the file should be included
        :param recursive: If True, search recursively through subdirectories. If False, only search the top-level directory
        :param include_hidden: If True, include hidden files (starting with .). Default is False
        :return: List of filepaths matching the criteria
        """
        if preset is not None:
            if isinstance(preset, FileManagerPresetType):
                preset_filter = self.PRESET_FILTERS[preset]
            else:
                preset_filter = self.custom_presets.get(preset)
                if preset_filter is None:
                    raise ValueError(f"Custom preset '{preset}' not found")

            extensions = preset_filter.extensions or extensions
            pattern = preset_filter.pattern or pattern
            content_check = preset_filter.content_check or content_check

        matching_files = []

        if recursive:
            for root, _, files in self.directory.walk():
                if not include_hidden and any(
                    part.startswith(".") for part in root.parts
                ):
                    continue
                matching_files.extend(
                    _filter_files(
                        root, files, extensions, pattern, content_check, include_hidden
                    )
                )
        else:
            files = self.directory.iterdir()
            files = [
                f.name for f in files if f.is_file()
            ]
            matching_files.extend(
                _filter_files(
                    self.directory,
                    files,
                    extensions,
                    pattern,
                    content_check,
                    include_hidden,
                )
            )

        return matching_files

    @staticmethod
    def is_image_file(filepath: str) -> bool:
        """Check if a file is an image based on its extension."""
        return any(
            filepath.lower().endswith(ext)
            for ext in FileManager.PRESET_FILTERS[
                FileManagerPresetType.IMAGES
            ].extensions
        )

    @staticmethod
    def is_tiff_file(filepath: str) -> bool:
        """Check if a file is a TIFF image."""
        return any(
            filepath.lower().endswith(ext)
            for ext in FileManager.PRESET_FILTERS[FileManagerPresetType.TIFF].extensions
        )

    @staticmethod
    def contains_text(filepath: str, text: str) -> bool:
        """Check if a file contains the specified text."""
        with open(filepath, "r") as file:
            return text in file.read()

    def list_available_presets(self) -> Dict[str, str]:
        """List all available presets and their descriptions"""
        presets = {
            preset.name: filter.description
            for preset, filter in self.PRESET_FILTERS.items()
        }
        presets.update(
            {name: filter.description for name, filter in self.custom_presets.items()}
        )
        return presets
