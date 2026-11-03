import os,csv, pandas as pd
from datetime import datetime as dt

# choice = input("what do you wanna do?")

tk_inp = float(input("enter expense (e.g 40.34)"))

path = './data/expense_calulator.csv'
# with open(path, 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(["Amount","Timestamp"])
#

df = pd.read_csv(path)
try:
    with open(path,'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([tk_inp, dt.now()])
except FileNotFoundError:
    print("file not exist")

try:
    with open(path,'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        print(f" print reader {reader}")
        print(f" reader rows")
        for row in reader:
            print(row)
except FileNotFoundError:
    print("file not exist")






