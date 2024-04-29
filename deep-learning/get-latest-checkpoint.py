from pathlib import Path
from os import listdir
from os.path import isdir


def get_latest_checkpoint(checkpoint_parent_dir):
    checkpoint_parent_dir = Path(checkpoint_parent_dir)
    checkpoint_dir_list = [
        x for x in listdir(checkpoint_parent_dir) if isdir(checkpoint_parent_dir / x)
    ]
    checkpoint_dir_list.sort(reverse=True)
    latest_checkpoint = checkpoint_parent_dir / checkpoint_dir_list[0]
    return latest_checkpoint
