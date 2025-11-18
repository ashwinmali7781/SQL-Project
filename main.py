from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL Connection
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Ashwin@7781",
    database="student_db"
)

cursor = db.cursor()

@app.route('/')
def home():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    return render_template('index.html', students=data)

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    roll_no = request.form['roll_no']
    course = request.form['course']   
    email = request.form['email']
    phone = request.form['phone']

    query = "INSERT INTO students (name, roll_no, course, email, phone) VALUES (%s, %s, %s, %s, %s)"
    values = (name, roll_no, course, email, phone)
    cursor.execute(query, values)
    db.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
