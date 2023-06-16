import csv
from datetime import datetime

filename = 'original1.csv'
filename_out = 'original1_out.csv'

with open(filename, 'r') as csvfile, open(filename_out, 'w') as csvfile_out:
    reader = csv.reader(csvfile)
    writer = csv.writer(csvfile_out)
    data = list(reader)

    for row in data[1:]:
        ts = datetime.strptime(row[0], "%Y")
        row[0] = ts.strftime('%Y-%m-%d')

    writer.writerows(data)

print(data)
