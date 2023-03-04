import csv
import sqlite3

# opening the connection to the database
conn = sqlite3.connect('football_data.db')
cur = conn.cursor()

# We shall drop all table data so in case we have to re run we ont repeat code
conn.execute('DROP TABLE IF EXISTS player_data')
print('player_data drop successful');

conn.execute('DROP TABLE IF EXISTS club_info')
print('club info drop successful');

# Create the table as it has been dropped
conn.execute('CREATE TABLE player_data (player_id INTEGER PRIMARY KEY, name TEXT, club_id INTEGER, current_club_name TEXT, country_of_citizenship TEXT, date_of_birth TEXT, position TEXT, FOREIGN KEY (club_id) REFERENCES club_info(club_id))')
print('table created successfully');

conn.execute('CREATE TABLE club_info (club_id INTEGER PRIMARY KEY, club_name TEXT,stadium_name TEXT )')
print('print table 2 created')

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
        position = row[8]

        cur.execute('INSERT INTO player_data VALUES (?,?,?,?,?,?,?)', (player_id, name, current_club_id, current_club_name, country_of_citizenship, date_of_birth, position))
        conn.commit()
print('database 1 parsed')



with open('clubs.csv', newline="") as f:
    reader2 = csv.reader(f, delimiter=',')
    next(reader2)  # skips the first iteration in this case the column name row
    for row in reader2:
        print(row)

        club_id = int(row[0])
        club_name = row[2]
        stadium_name = (row[10])


        cur.execute('INSERT INTO club_info VALUES (?,?,?)', (club_id, club_name, stadium_name))
        conn.commit()
print('database 2 parsed')


conn.close()




