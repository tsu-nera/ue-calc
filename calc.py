import pandas as pd

file_path = './data/sample.csv'

df = pd.read_csv(file_path, index_col='乗車 ID')

print(df)
