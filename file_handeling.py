# ✅ Found {data_path}")
# ❌ Cannot find {data_path}")



choice = int(input("what do you wanna do? "))

match(choice):
    case(0):
        import os
        import json

        path = './data/historic_data.csv'
        file_exists = os.path.exists(path)

        if file_exists:
            print(f'path exists?-{file_exists}')

            with open(path, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    print(line)
        else:
            print('path does not exist')

        print(f"Current working directory: {os.getcwd()}")
    case(1):
        import os
        path = './data/historic_data.csv'
        file_exists = os.path.exists(path)
        if file_exists:
            print(f'path exists?-{file_exists}')
            with open(path, 'r') as f:
                content = f.read()
                print(content)
    case(2):
        import sys
        print(sys.path)
    case(3):
        import os,csv
        path = './data/new_csv.csv'
        file_exists = os.path.exists(path)
        print(f'path exists?-{file_exists}')
        os.makedirs('.data', exist_ok=True)
        with open(path, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['date', 'open', 'high', 'low', 'close', 'volume'])
            # writer.writerow(['2'])
        with open(path, 'r') as f:
            csv_reader = csv.reader(f)