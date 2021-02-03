This is a dashboard for city officials to see how long the the response time to complaints is.

The nyc_data_cleaning.py file is a script to subset the original data into a dataset that contains only the columns for identification number, date filed, date closed, and zipcode. Currently the complaints for which there is no zipcode on file have been removed.

The nyc_data_processing.py file is a script to find the time difference between filing and closing for each complaint.

TO-DOs:
- finish writing data README