import pandas as pd

def aggregate_mean(df, column):
    return df.groupby("class")[column].mean().to_dict()

def pipeline(column):
    data = pd.read_csv("SOME_VERY_LARGE_FILE.csv")
    data = aggregate_mean(data, column)
    return data