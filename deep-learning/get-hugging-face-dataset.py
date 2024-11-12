from datasets import load_dataset, config

# Download path
print(config.HF_DATASETS_CACHE)

dataset = load_dataset("Open-Orca/FLAN", data_dir="flan_fsnoopt_data")

print(dataset)
"""
DatasetDict({
    train: Dataset({
        features: ['inputs', 'targets', '_template_idx', '_task_source', '_task_name', '_template_type'],
        num_rows: 34258827
    })
})
"""

print(dataset["train"].features)
"""
{'inputs': Value(dtype='string', id=None),
 'targets': Value(dtype='string', id=None),
 '_template_idx': Value(dtype='int64', id=None),
 '_task_source': Value(dtype='string', id=None),
 ...}
"""

unique_values = sorted(dataset["train"].unique("target_label"))