import pandas as pd
import os
from datetime import datetime

in_file_path = os.path.join(os.path.abspath('../data'),'subsetted_nyc_data.csv')

df = pd.read_csv(in_file_path)

#Remove any requests that have yet to be closed (are still open)
df.dropna(axis=0, how='any', subset=['time_closed'], inplace=True)

def month_closed(time_closed):
    date_format = '%m/%d/%Y %I:%M:%S %p'
    month = datetime.strptime(time_closed, date_format).month
    #print month
    return month

df['month_closed'] = map(month_closed, df['time_closed'])

#Calculate time difference and append in correct column
def time_difference(later_str_time, earlier_str_time):
    date_format = '%m/%d/%Y %I:%M:%S %p'
    time2 = datetime.strptime(later_str_time, date_format)
    time1 = datetime.strptime(earlier_str_time, date_format)
    diff = (time2 - time1).total_seconds()
    #print(diff)
    return diff

df['time_diff'] = map(time_difference, df['time_closed'], df['time_filed'])

#Calculate monthly average for each zipcode
df_averages_by_zipcode = df.groupby(['zipcode', 'month_closed'])['time_diff'].mean().reset_index()

df_all_monthly_averages = df.groupby('month_closed')['time_diff'].mean().reset_index()

df_averages_by_zipcode.to_csv(os.path.join(os.path.abspath('../data'),'average_times_zipcode.csv'))
df_all_monthly_averages.to_csv(os.path.join(os.path.abspath('../data'),'average_times_all.csv'))
