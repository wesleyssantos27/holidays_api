import requests as re
import pandas as pd
import json

years=(2020,2021,2022,2023)
holidays_df = pd.DataFrame(columns=['name','description','date','week_day_name'])
holidays_df

for year in years:
    parameters = {
            'api_key':'b9928b208bec22ffc1eb5adedf95725df47acad9',
            'country':'br',
            'year':year
            }
    
    api_return = re.get(
    'https://calendarific.com/api/v2/holidays',
    params=parameters
    )
    
    dict_return = json.loads(api_return.text)
    
    df = pd.DataFrame.from_dict(dict_return['response']['holidays'])
    df['date'] = df['date'].apply(lambda x: str(x)[9:19])
    df['week_day_name'] = df['date'].apply(lambda x: pd.Timestamp(x).strftime('%A'))
    df = df[['name','description','date','week_day_name']]
    
    holidays_df = pd.concat([holidays_df, df])

holidays_df[['name','description','date','week_day_name']].to_csv('./feriados_brasil.csv', index=False, sep=';')

