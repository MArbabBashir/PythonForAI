import pandas as pd

from datetime import datetime as dt
import os


path = './testyourselfforwritingintocsv/data.csv'
now = dt.now()

if not os.path.exists(path) or os.path.getsize(path) == 0:
    # make file ---done and make header
    os.makedirs(os.path.dirname(path))
    df =  pd.DataFrame(columns =["Id", "Name", "Category", "Amount", "Timestamp" ])
    df.to_csv(path, index=False)

def read_csv():
    rd = pd.read_csv(path)
    return rd

def write_to_csv():
    tk_name = input("Please enter the name of the csv file: ")
    tk_cat = input("Please enter the category of the csv file: ")
    tk_amount = float(input("Please enter the amount of the csv file: "))
    df = pd.DataFrame([["5", tk_name, tk_cat, tk_amount, str(now)]])
    df.to_csv(path, mode= 'a', index=False)


def update_csv():
    tk_name = input("Please enter the name of the csv file: ")
    tk_amnt = int(input("Please enter the amount of the csv file: "))

    rd = pd.read_csv(path)
    mask = rd["Name"].str.lower() == tk_name.lower()
    rd.loc[mask,"Amount"] = tk_amnt
    rd.to_csv(path, index=False)



while True:

    choice = input("\n 1. read(r) \n 2. write(w) \n 3. update(c) \n 4. exit \n Enter your choice: __")
    match choice:
        case "r":
            print(read_csv())
        case "w":
            write_to_csv()
        case "u":
            update_csv()
        case "_":
            print("Invalid choice")


# def delete_expense():
#     print("Please enter the name of the csv file you would like to delete: ")

# print("im here")
#
# latitude= 24.8607
# longitude=67.0011
# current_weather = True
# url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}"
#
#
#
#
# response = rq.get(url)
# data = response.json()
#
# print(data)

# Expenditure
#  Id   Name     Category    Amount     timestamp

