import pandas as pd
import os
from datetime import datetime

in_file_path = os.path.join(os.path.abspath('../data'),'subsetted_nyc_data.csv')
df = pd.read_csv(in_file_path)

#Remove any requests that have yet to be closed (are still open)
df.dropna(axis=0, how='any', subset=['time_closed'], inplace=True)

#Calculate time difference and append in correct column
def time_difference(later_str_time, earlier_str_time):
    date_format = '%m/%d/%Y %I:%M:%S %p'
    time2 = datetime.strptime(later_str_time, date_format)
    time1 = datetime.strptime(earlier_str_time, date_format)
    #print(time2 - time1)
    return time2 - time1

df['time_diff'] = map(time_difference, df['time_closed'], df['time_filed'])

print(df)

#next steps: create a dataframe with the average wait time for each month of the year
