import csv
from datetime import datetime

with open('original2.csv', 'w') as file:
    writer = csv.writer(file)
    field = ["year", "region", "value"]

    writer.writerow(field)
    writer.writerow(["20200131", "Almaty", "130500"])
    writer.writerow(["20200131", "Almaty", "150500"])

filename = 'original2.csv'
filename_out = 'original2_out.csv'
row_sum = 0

with open(filename, 'r') as csvfile, open(filename_out, 'w') as csvfile_out:
    reader = csv.reader(csvfile)
    writer_out = csv.writer(csvfile_out)
    data = list(reader)

    for row in data[1:]:
        ts = datetime.strptime(row[0], "%Y%m%d")
        row[0] = ts.strftime('%d-%m-%Y')
        row_value = int(row[2])
        row_sum = row_value + row_sum

    data[-1][-1] = str(row_sum)
    writer_out.writerows(data[::len(data)-1])

print(data[-1])
