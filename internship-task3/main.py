import csv
from datetime import datetime
import re

with open('original3.csv', 'w') as file:
    writer = csv.writer(file)
    field = ["year", "region", "value"]

    writer.writerow(field)
    writer.writerow(["Reported on 2022, May 1st", "Almaty", "130500"])
    writer.writerow(["Reported on 2022, August 3rd", "Astana", "150500"])

filename = 'original3.csv'
filename_out = 'original3_out.csv'


with open(filename, 'r') as csvfile, open(filename_out, 'w') as csvfile_out:
    reader = csv.reader(csvfile)
    writer_out = csv.writer(csvfile_out)
    data = list(reader)

    for row in data[1:]:
        date_string = row[0].split(', ')
        year_text = date_string[0]
        year_pattern = r"(?:19|20)\d{2}"
        year = (re.findall(year_pattern, year_text))[0]

        date_text = date_string[1]
        month_pattern = r"(January|February|March|April|May|June|July|August|September|October|November|December)"
        day_pattern = r"\d+"
        month = re.search(month_pattern, date_text).group(0)
        day = re.search(day_pattern, date_text).group(0)
        day = day.zfill(2)

        fulldate = f"{year} {month} {day}"
        ts = datetime.strptime(fulldate, "%Y %B %d")
        fulldate_out = ts.strftime('%Y-%m-%d')
        row[0] = fulldate_out
    writer_out.writerows(data)

print(data[0])
