from dataflows import Flow, unpivot
import csv


# Create initial CSV file
with open('task5_dataflows.csv', 'w') as in_file:
    data = [
        {'place': 'Almaty', '2021': 40000, '2022': 6000, '2023': 5000},
        {'place': 'Astana', '2021': 50000, '2022': 6000, '2023': 5000},
        {'place': 'Aktau', '2021': 50000, '2022': 6000, '2023': 5000}]
    fieldnames = ['place', '2021', '2022', '2023']

    writer = csv.DictWriter(in_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

# Unpivot the table
unpivoting_fields = [{'name': '([0-9]{4})', 'keys': {'date': r'\1'}}]
extra_keys = [{'name': 'date', 'type': 'year'}]
extra_value = {'name': 'value', 'type': 'integer'}

result = Flow(data, unpivot(unpivoting_fields, extra_keys, extra_value)).results()[0][0]

# Replace 'place' with 'city' to match target output
for row in result:
    row['city'] = row.pop('place')


# Write to new CSV file
with open('task5_dataflows_out.csv', 'w') as out_file:
    fieldnames = ['date', 'city', 'value']
    writer = csv.DictWriter(out_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(result)
