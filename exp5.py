'''Name Ayush Gupta
SapID: 500125537'''
def perform_eda(df):
    
    print("\nDataset Info:")
    print(df.info())


    print("\nMissing Values in Dataset:")
    print(df.isnull().sum())

    print("\nStatistical Summary:")
    print(df.describe())

    print("\nCorrelation Matrix:")
    print(df.corr())

   
perform_eda(df)
