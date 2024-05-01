from pathlib import Path
import glob
import json

"""
What is does: collects list of arrow files in a local Hugging Face dataset directory.
Purpose: to load dataset for every split without hassle.
Usage:
dataset_info = HFDatasetInfo(data_path)
arrow_files = dataset_info.arrow_files
# {'train': [
#   '<data_path>/train/data-00000-of-00003.arrow',
#   '<data_path>/train/data-00001-of-00003.arrow',
#   '<data_path>/train/data-00002-of-00003.arrow'
#   ],
#  'test': [
#   '<data_path>/test/data-00000-of-00002.arrow',
#   '<data_path>/test/data-00001-of-00002.arrow']}
"""


class HFDatasetInfo:
    def __init__(self, dataset_path):
        self.dataset_path = Path(dataset_path)
        self.splits = self.get_split_list()
        self.states = self.get_state_info()
        self.arrow_files = self.get_arrow_file_list()

    def get_split_list(self):
        dataset_dict_path = glob.glob(str(self.dataset_path / "dataset_dict.json"))[0]
        with open(dataset_dict_path) as f:
            dataset_dict = json.load(f)
        return dataset_dict["splits"]

    def get_state_info(self):
        split_list = self.get_split_list()
        state_info_dict = dict()
        for split in split_list:
            state_path = glob.glob(str(self.dataset_path / split / "state.json"))[0]
            with open(state_path) as f:
                state_info = json.load(f)
            state_info_dict[split] = state_info
        return state_info_dict

    def get_arrow_file_list(self):
        arrow_file_dict = dict()
        for split in self.splits:
            arrow_file_list = []
            for entry in self.states[split]["_data_files"]:
                file_path = self.dataset_path / split / entry["filename"]
                arrow_file_list.append(str(file_path))
            arrow_file_dict[split] = arrow_file_list
        return arrow_file_dict
