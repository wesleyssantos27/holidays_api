import calendarific
import pandas as pd

holidays_df = pd.DataFrame(columns=['name','description','date','week_day_name'])
calapi = calendarific.v2('b9928b208bec22ffc1eb5adedf95725df47acad9')

for year in (2020,2021,2022,2023):
    parameters = {
        # Required
        'country': 'BR',
        'year':    year,
    }

    holidays = calapi.holidays(parameters)

    df = pd.DataFrame.from_dict(holidays['response']['holidays'])
    df['date'] = df['date'].apply(lambda x: str(x)[9:19])
    df['week_day_name'] = df['date'].apply(lambda x: pd.Timestamp(x).strftime('%A'))
    df = df[['name','description','date','week_day_name']]
        
    holidays_df = pd.concat([holidays_df, df])

holidays_df[['name','description','date','week_day_name']].to_csv('./feriados_brasil_library.csv', index=False, sep=';')