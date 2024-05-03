import glob
import tarfile
from tqdm import tqdm
from pathlib import Path

"""
What is does: extract specific files from tar.xz files in a directory.
Purpose: to save disk space by avoiding unnecessary file extractions.
Usage:
dir_path = "./research/checkpoints/"
targets = [".json", ".arrow"]
extract_specific_files_from_tar(dir_path, targets)
"""


def extract_specific_files_from_tar(dir_path: str, targets: list[str]):
    if dir_path[-1] == "/":
        dir_path = dir_path[:-1]
    glob_pattern = f"{dir_path}/*.tar.xz"
    tar_files = glob.glob(glob_pattern)
    for tar in tqdm(tar_files):
        with tarfile.open(tar) as t:
            members = t.getmembers()
            for m in members:
                if any(t in m.name for t in targets):
                    extraction_path = Path(tar).name.split(".")[0]
                    m.name = Path(m.name).name
                    print(f"{Path(tar).name}: {m.name}")
                    t.extract(m, path=f"./{extraction_path}")
