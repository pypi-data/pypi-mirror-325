import re
import tifffile
import sys
import csv
from .file_manager import FileManager # ensure that we load local file manager
from pathlib import Path
from natsort import natsorted


def extract_value(tag: str, string: str) -> str | None:
    pattern = re.compile(rf'{tag}(\d+\.?\d*)')
    match = pattern.search(string)
    if match:
        return match.group(1)
    return None


def extract_string_value(tag: str, string: str) -> str | None:
    pattern = re.compile(rf'{tag}(\"\d+?\.?\d*\")')
    match = pattern.search(string)
    if match:
        return match.group(1)
    return None


def extract_float_value(tag: str, string: str) -> float | None:
    value = extract_value(tag, string)
    if value:
        try:
            return float(value)
        except ValueError:
            print(f"Could not convert {value} from {tag} to float.")
            return
    return


def extract_int_value(tag: str, string: str) -> int | None:
    value = extract_string_value(tag, string)
    if value:
        try:
            return int(value.replace('\"', ''))
        except ValueError:
            print(f"Could not convert {value} from {tag} to float.")
            return
    return


if __name__ == '__main__':
    if not sys.argv[2].endswith(".csv"):
        print("Second argument should end with .csv")
        sys.exit()
    else:
        csv_filename = sys.argv[2]

    manager = FileManager(sys.argv[1])
    files = manager.list_files(extensions=["tif"])
    files = natsorted(files)

    ome_metadatas = [tifffile.TiffFile(file).ome_metadata for file in files]

    data = [{'file_name': Path(file).stem,
             'slice_number': extract_int_value('FirstZ=', ome_metadata),
             'x_position': extract_float_value('<M K="x">', ome_metadata),
             'y_position': extract_float_value('<M K="y">', ome_metadata),
             'z_position': extract_float_value('<M K="z">', ome_metadata),
             'defocus_position': extract_float_value('<M K="extra">', ome_metadata)}
            for (file, ome_metadata) in zip(files, ome_metadatas)]

    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['file_name', 'slice_number', 'x_position', 'y_position', 'z_position', 'defocus_position']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)





