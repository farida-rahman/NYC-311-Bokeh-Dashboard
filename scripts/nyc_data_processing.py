import pandas as pd
import os
from datetime import datetime

in_file_path = os.path.join(os.path.abspath('data'),'subsetted_nyc_data.csv')
df = pd.read_csv(in_file_path)

#finish this format
date_format = '%m/%d/%Y %I:%M:%S %p'

#Created a column for time difference in the df
df['time_diff'] = ''

#Remove any requests that have yet to be closed (are still open)
df.dropna(axis=0, how='any', subset=['time_closed'], inplace=True)

#Calculate time difference and append in correct column
for index, values in df.iterrows():
    time2 = datetime.strptime(values[2], date_format)
    time1 = datetime.strptime(values[1], date_format)
    values['time_diff'] = time2 - time1

print(df)


#next steps: finish datetime format, calculuate time delta for each time and append as a new column to the dataframe, create a dataframe with the average wait time for each month of the year
