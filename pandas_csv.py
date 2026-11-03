import os
from datetime import datetime as dt
import pandas as pd

path =  './csv_data/result.csv'
df = pd.DataFrame(columns=["Name", "Category", "Amount", "Timestamp"])
now = dt.now()


if not os.path.exists(path) or os.path.getsize(path) == 0:
    print(f"{path} does not exist. Creating directory")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    print(f"---------{path} created--------")
    print(f"----creating Header : {df}-----")
    df.to_csv(path, index=False)
else:
    print(f"----{path} already exists!!!----")
    print(f"---- header already exists !!! \n {df.columns[[0,1,2,3]]} as----")

def add_row():

    try:
        tk_name = input("Enter Expenditure name : ")
        tk_amount = int(input("Enter amount : "))
        tk_category = input("Enter category : ")

        add_itm =pd.DataFrame([[tk_name, tk_category, tk_amount, now]])
        add_itm.to_csv(path, mode='a', header=False, index=False)

    except TypeError as te:
        print(f"file not exist {te}")

def read_csv():
    csv_out = pd.read_csv(path)
    print("======== CSV File Read==========")
    print(csv_out)

def update_row():
    try:
        tk_name = input("Enter Expenditure name : ")
        # tk_amount = int(input("Enter amount : "))

        out = pd.read_csv(path)
        matched = out["Name"] == tk_name
        # and out["amount"] == tk_amount

        if not matched.any():
            print(f"No record found with the Name {tk_name}")
            return
        print(f" records found with the name {tk_name}")
        tk_updated_name = input("Enter Expenditure name : ")
        tk_updated_amount = int(input("Enter amount : "))

        out.loc[matched, "Name"] = tk_updated_name
        out.loc[matched, "Amount"] = tk_updated_amount
        out.loc[matched, "Timestamp"] = str(now)


        out.to_csv(path, index=False)

        updated_row = out[matched]
        print(f"======Update row: {updated_row}====")



        print("updated successfully")

    except KeyError as te:
        print(f"Key-Error {te}")

def delete_row():
    tk_name = input("Enter Expenditure name : ")
    out = pd.read_csv(path)
    matched = out["Name"] == tk_name

    deleted_row = out[matched]


    if not matched.any():
        print(f"No record found with the Name {tk_name}")
        return

    out.drop(out[matched].index, inplace =True)
    out.to_csv(path, index=False)

    print(f"======Deleted row output: {deleted_row}====")




while True:
    choice = input("\n What do you want to do Read(r), Add Expenditure(a), Update(u), Delete(d), Exit(e): ")
    match choice:
        case "r":
            read_csv()
        case "a":
            add_row()
        case "u":
            update_row()
        case "d":
            delete_row()
        case "e":
            break