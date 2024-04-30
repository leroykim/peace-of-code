from datasets import Dataset, DatasetDict

"""
What is does: checking longest input length of tokenized dataset.
Purpose: to see how many tokenized inputs exceed maximum length of a model or tokenizer.
Usage:
get_length_info_all(
    datasetdict=text_dataset, set_list=["train", "test", "valid"], max_length=128
)
"""


def get_length_info(dataset: Dataset, set_name: str, max_length=512):
    longest = 0
    length_sum = 0
    overflow_rows = 0
    for row in dataset.iter(batch_size=1):
        length = len(row["input_ids"][0])
        length_sum += length
        if length > longest:
            longest = length
        if length > max_length:
            overflow_rows += 1
    average = length_sum / dataset.num_rows
    print(f"Longest in {set_name} set = {longest}.")
    print(f"Average in {set_name} set = {average}.")
    print(f"# rows longer than {max_length} = {overflow_rows}.")
    return longest, average, overflow_rows


def get_length_info_all(datasetdict: DatasetDict, set_list: list[str], max_length=512):
    average_sum = 0
    longest_of_all = 0
    total_overflow_rows = 0
    for set_name in set_list:
        (longest, average, overflow_rows) = get_length_info(
            datasetdict[set_name], set_name, max_length
        )
        average_sum += average
        if longest > longest_of_all:
            longest_of_all = longest
        total_overflow_rows += overflow_rows
    total_average = average_sum / len(set_list)
    print(f"Longest of all is {longest_of_all}.")
    print(f"Total average is {total_average}.")
    print(f"Total # rows longer than {max_length} = {overflow_rows}.")
