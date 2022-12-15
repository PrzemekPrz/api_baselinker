import time
import pandas as pd
import requests
import json

unix = []
first_day = #Enter the date format UNIX
last_day = #Enter the date format UNIX

while first_day != last_day:
    unix.append(first_day)
    first_day = first_day + 7200 #(2h)

container = []

for i in unix:
    counter = 10
    while counter != 0:
        counter = counter - 1
        time.sleep(1)
    print(f'Add: {i}')
    data = {
        'token': '',
        'method': 'getInvoices',
        'parameters': f'{{"date_from": {i}}}'
    }
    response = requests.post('https://api.baselinker.com/connector.php', data=data)
    baza = json.loads(response.text)
    container.append(baza)

df = pd.DataFrame(container)
df.to_json(r'./data.json')