from load_dataset import features1, features2, features3, features4, features5, features6
import pandas as pd

def heuristic_filter(features, string_columns, threshold=1):
    """
    Filter rows based on a heuristic that sums numerical feature values.
    Additionally, removes datasets with all zero values and benign categories (case-insensitive).

    Parameters:
    - features: DataFrame containing the features.
    - string_columns: List of string column names to keep constant.
    - threshold: Minimum sum of numerical values for a row to be retained.

    Returns:
    - Filtered DataFrame or None if it should be ignored.
    """
    # Separate string and numerical data
    string_data = features[string_columns]
    numerical_data = features.drop(columns=string_columns)

    # Apply threshold-based filtering
    filtered_numerical = numerical_data[numerical_data.sum(axis=1) >= threshold]

    # Recombine with string columns
    filtered = pd.concat([string_data.loc[filtered_numerical.index], filtered_numerical], axis=1)

    # Ignore dataset if all numerical values are zero after filtering
    if filtered.drop(columns=string_columns).sum().sum() == 0:
        print("Skipping dataset with all zero values...")
        return None  # Ignore dataset

    # Ignore dataset if it contains 'benign' (case-insensitive)
    if filtered["category"].str.lower().str.contains("benign").any():
        print("Skipping benign dataset...")
        return None  # Ignore dataset

    print(f"Filtered dataset shape: {filtered.shape}")
    return filtered

# List of datasets to process
datasets = [features1, features2, features3, features4, features5, features6]

# Filter datasets and remove ignored ones
filtered_datasets = []


for dataset in datasets:
    filtered_data = heuristic_filter(dataset, ['category', 'specific_class'])
    if filtered_data is not None:
        filtered_datasets.append(filtered_data)