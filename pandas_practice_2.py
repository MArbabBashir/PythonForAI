import os
import pandas as pd

path_xlsx = 'historic_data.xlsx'
file_exists_xlsx = os.path.exists(path_xlsx)

if file_exists_xlsx:
    print(f'file exists?-{file_exists_xlsx}')
else:
    print(f'file not exists?-{file_exists_xlsx}')

df = pd.read_excel(path_xlsx)

print(f"df res: \n \t {df}")
print(f"df res.max: \n \t {df.max()}")

