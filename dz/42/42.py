import csv

cs = [
	['hostnsme', 'vendor', 'model', 'Location'],
	['sw1', 'Cisco', '3750', 'London'],
	['sw2', 'Cisco', '3850', 'Liverpool'],
	['sw3', 'Cisco', '3650', 'Liverpool'],
	['sw4', 'Cisco', '3650', 'London']
]

with open('data2.csv', 'w') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(cs)
    
with open('data2.csv') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        print(row)