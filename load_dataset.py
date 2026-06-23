import pandas as pd

def load_data(file_path):
    """Load dataset from a CSV file."""
    return pd.read_csv(file_path)

def preprocess_data(data):
    """Preprocess the dataset by selecting relevant features."""
    # Select relevant features (Timestamps and Payload Information)
    return data[['DATA_0', 'DATA_2','category', 'specific_class']]

#from google.colab import files
#uploaded = files.upload()

# Load the dataset
data1 = load_data('dataset/decimal_DoS.csv')
data2 = load_data('dataset/decimal_benign.csv')
data3 = load_data('dataset/decimal_spoofing-GAS.csv')
data4 = load_data('dataset/decimal_spoofing-RPM.csv')
data5 = load_data('dataset/decimal_spoofing-SPEED.csv')
data6 = load_data('dataset/decimal_spoofing-STEERING_WHEEL.csv')

# Preprocess the dataset and print the results
features1 = preprocess_data(data1)
features2 = preprocess_data(data2)
features3 = preprocess_data(data3)
features4 = preprocess_data(data4)
features5 = preprocess_data(data5)
features6 = preprocess_data(data6)

if __name__ == "__main__":
    print("Dataset 1 loaded with shape:", features1.shape)
    print("Dataset 2 loaded with shape:", features2.shape)
    print("Dataset 3 loaded with shape:", features3.shape)
    print("Dataset 4 loaded with shape:", features4.shape)
    print("Dataset 5 loaded with shape:", features5.shape)
    print("Dataset 6 loaded with shape:", features6.shape)