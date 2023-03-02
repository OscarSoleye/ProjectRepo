import csv

with open('players.csv', newline="") as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)#skips the first iteration in this case the column name row
    for row in reader:
        print(row)