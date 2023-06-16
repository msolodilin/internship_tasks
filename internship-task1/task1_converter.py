import csv
from datetime import datetime

filename = 'original1.csv'
filename_out = 'original1_out.csv'

with open(filename, 'r') as csvfile, open(filename_out, 'w') as csvfile_out:
    datareader = csv.reader(csvfile)
    datawriter = csv.writer(csvfile_out)
    next(csvfile)
    for row in datareader:
            ts = datetime.strptime(row[0], "%Y")
            row[0] = ts.strftime('%Y-%m-%d')
            datawriter.writerow(row)
    print(row)
