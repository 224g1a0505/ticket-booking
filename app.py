from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bookings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    time TEXT,
                    date TEXT,
                    persons INTEGER,
                    seat_no INTEGER
                )''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect('/book')
    return render_template('login.html')

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        name = request.form['name']
        time = request.form['time']
        date = request.form['date']
        persons = request.form['persons']
        seat_no = request.form['seat_no']

        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO bookings (name, time, date, persons, seat_no) VALUES (?, ?, ?, ?, ?)",
                  (name, time, date, persons, seat_no))
        conn.commit()
        conn.close()

        return render_template('success.html', name=name)
    return render_template('book.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
