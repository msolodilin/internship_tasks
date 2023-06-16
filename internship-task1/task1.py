import csv

with open('original1.csv', 'w') as file:
    writer = csv.writer(file)
    field = ["year", "region", "value"]

    writer.writerow(field)
    writer.writerow(["2020", "Almaty", "130500"])
    writer.writerow(["2021", "Almaty", "150500"])


#%%

#%%
