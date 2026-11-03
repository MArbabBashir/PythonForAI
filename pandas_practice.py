import pandas as pd
import os

file_path_xlsx = 'historic_data.xlsx'

file_path_csv = 'historic_data.csv'
file_exists = os.path.exists(file_path_csv)
if file_exists:
    print(f"file exits? {file_exists}")
else:
    print(f"file exits? {file_exists}")

df = pd.read_csv(file_path_csv)
print(df)

df.to_excel(file_path_xlsx, index=False)


file_exists_xlsx = os.path.exists(file_path_xlsx)
if file_exists_xlsx:
    print(f"file exits? {file_exists_xlsx}")
else:
    print(f"file exits? {file_exists_xlsx}")
