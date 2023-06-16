import csv
from datetime import datetime

with open('original2.csv', 'w') as file:
    writer = csv.writer(file)
    field = ["year", "region", "value"]

    writer.writerow(field)
    writer.writerow(["20200131", "Almaty", "130500"])
    writer.writerow(["20200131", "Almaty", "150500"])




#%%
