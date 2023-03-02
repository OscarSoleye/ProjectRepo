import csv
import sqlite3

# opening the connection to the database
conn = sqlite3.connect('football_data.db')
cur = conn.cursor()

# We shall drop all table data so in case we have to re run we ont repeat code
conn.execute('DROP TABLE IF EXISTS player_data')
print('player_data drop successful');

# Create the table as it has been dropped
conn.execuute('CREATE TABLE player_data (player_id INTEGER, name TEXT, current_club_id INTEGER, current_club_name TEXT, country_of_citizenship TEXT, date_of_birth TEXT, position TEXT,foot TEXT,height_in_cm REAL,current_club_domestic_competition_id INTEGER,image_url TEXT'))
print('table created successfully');

# read the csv file
with open('players.csv', newline="") as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)  # skips the first iteration in this case the column name row
    for row in reader:
        print(row)

        player_id = int(row[0])
        name = row[1]
        current_club_id = int(row[2])
        current_club_name = row[3]
        country_of_citizenship = row[4]
        date_of_birth = row[7]
        position =
        foot
        height_in_cm
        current_club_domestic_competition_id
        image_url


