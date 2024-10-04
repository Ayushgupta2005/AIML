
import pandas as pd

def import_and_show_data_details(file_path):
    
    df = pd.read_csv(file_path)

    print("Number of rows and columns:", df.shape)
    print("\nFirst 5 rows of the dataset:\n", df.head())
    print("\nSize of the dataset (number of elements):", df.size)
    print("\nNumber of missing values in each column:\n", df.isnull().sum())

    print("\nDescriptive Statistics for Numerical Columns:")
    print("Sum:\n", df.sum(numeric_only=True))
    print("Average:\n", df.mean(numeric_only=True))
    print("Minimum values:\n", df.min(numeric_only=True))
    print("Maximum values:\n", df.max(numeric_only=True))


    df.to_csv("exported_dataset.csv", index=False)
    print("\nDataset has been exported to 'exported_dataset.csv'.")
    
    return df

file_path = 'your_file.csv'
df = import_and_show_data_details(file_path)
