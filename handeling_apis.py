#
# # python -m venv .venv
# # .\.venv\Scripts\Activate.ps1
# # python -m pip install requests
#
import requests
import os
from datetime import datetime, timedelta
import pandas as pd
today = datetime.now()
week_ago = today - timedelta(days=7)

start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

try:
    url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

    res = requests.get(url)

    data = res.json()
    print(data.keys())

    daily_data = data['daily']
    print(daily_data)

    df = pd.DataFrame(daily_data)
    df.to_csv('meteo_data.csv', index=False)
    print("Data saved")

except Exception as e:
    print(e)





# if not os.path.exists('data'):
#     os.makedirs('data')
# data.to_csv('data/weather_data.csv', index=False)
# print("data saved to data/weather_data.csv")

