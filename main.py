from flask import Flask, render_template
import sqlite3

main = Flask(__name__)

@main.route('/')
def index():
        # open the connection to the database
        conn = sqlite3.connect('football_data.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("select * from player_data")
        rows = cur.fetchall()
        conn.close()
        return render_template('index.html', rows=rows)

@main.route('/clubs')
def club():
        # open the connection to the database
        conn = sqlite3.connect('football_data.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("select * from club_info")
        rows = cur.fetchall()
        conn.close()
        return render_template('clubs.html', rows=rows)



@main.route('/players')
def players():
        # open the connection to the database
        conn = sqlite3.connect('football_data.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("select * from player_data")
        rows = cur.fetchall()
        conn.close()
        return render_template('players.html', rows=rows)

if __name__ == '__main__':
    main.run(debug=True)