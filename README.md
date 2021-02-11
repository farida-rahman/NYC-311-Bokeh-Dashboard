This is a dashboard for city officials to see how long the the response time to complaints is.

The initial dataset is a trimmed down version including only requests from 2020.

The nyc_data_cleaning.py file is a script to subset the original data into a dataset that contains only the columns for identification number, date filed, date closed, and zipcode. Currently the complaints for which there is no zipcode on file have been removed.

The nyc_data_processing.py file is a script to find the monthly average time difference between filing and closing for each zipcode and then all zipcodes. Any requests not currently closed get removed. Currently, the request is being counted in the month that it is closed.

TO-DOs:
- finish writing data README

In the future:
- inlcude all years, not just 2020 (this would involve appending a year column to the averages df as well)
