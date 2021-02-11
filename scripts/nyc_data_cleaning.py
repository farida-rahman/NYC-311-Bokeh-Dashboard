'''
TO-DO:
- Use data from the internet that gives a zipcode for the corresponding latitude aand longitude to fill in the missing zipcode information (need to redo the file reading and take out the line that filters out rows without a value for zipcode)
'''

import csv
import os.path

in_file_path = os.path.join(os.path.abspath('../data'),'nyc_data.csv')
outfile = os.path.join(os.path.abspath('../data'), 'subsetted_nyc_data.csv')

with open(in_file_path) as f, open(outfile, 'w') as o:
    reader = csv.reader(f)
    writer = csv.writer(o, delimiter = ',')
    headers = ['identification_code', 'time_filed', 'time_closed', 'zipcode']
    writer.writerow(headers)
    for row in reader:
        #row[8] refers to the column in the initial data with the zipcodes
        if row[8] != "":
            writer.writerow([row[0], row[1], row[2], row[8]])
            #see headers above for corresponding column number identification

print('done')
