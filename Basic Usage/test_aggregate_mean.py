import pandas as pd

def load_data():
    data = pd.DataFrame([[0, 2, 7, 4, 8],
                         [1, 7, 6, 3, 7],
                         [1, 1, "None", 8, 9],
                         [0, 2, 3, "None", 6],
                         [0, 5, 1, 4, 9]], 
                        columns = [f"feature_{i}" if i!=0 
                                  else "class" for i in range(5)])
    return data

def aggregate_mean(df, column):
    return df.groupby("class")[column].mean().to_dict()

def test_aggregate_mean_feature_1():   
    data = load_data()
    expected = {0: 3, 1: 4}
    result = aggregate_mean(data, "feature_1")
    assert expected == result