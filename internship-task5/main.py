import csv

# Create initial CSV file
with open('task5.csv', 'w') as initial_file:
    writer = csv.writer(initial_file)
    data = [['place', '2021', '2022', '2023'],
            ['Almaty', 40000, 6000, 5000],
            ['Astana', 50000, 6000, 5000],
            ['Aktau', 50000, 6000, 5000]]
    writer.writerows(data)

# Unpivot data
with open("task5.csv", "r") as in_file:
    reader = csv.reader(in_file)
    data = list(reader)

unpivoted_data = []
header = data[0]

for row in data[1:]:
    city = row[0]
    for i in range(1, len(header)):
        date = header[i]
        value = row[i]
        unpivoted_data.append([date, city, value])

# Write to new CSV file
with open('task5_out.csv', 'w') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(('date', 'city', 'value'))
    writer.writerows(unpivoted_data)
