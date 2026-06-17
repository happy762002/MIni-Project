from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL database configuration
db_config = {
    'host': 'localhost',  # Your MySQL host (localhost if MySQL is on the same machine)
    'user': 'root',  # Your MySQL username
    'password': 'your_password',  # Your MySQL password
    'database': 'student_info'  # The database you're using
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    id_number = request.form.get('name')  # Assuming you have 'name' for ID number
    first_name = request.form.getlist('name')[1]  # Assuming 'name' contains first name in the list
    last_name = request.form.getlist('name')[2]  # Assuming 'name' contains last name in the list
    email = request.form['email']
    phone = request.form['phone']
    gender = request.form.get('gender')
    city = request.form['city']
    dob = request.form['dob']
    terms = 1 if request.form.get('terms') == 'on' else 0

    # Connect to MySQL
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Insert data into the MySQL table
    cursor.execute("""
        INSERT INTO USERS (id_number, first_name, last_name, email, phone, gender, city, dob, terms)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (id_number, first_name, last_name, email, phone, gender, city, dob, terms))

    # Commit the transaction and close the connection
    conn.commit()
    cursor.close()
    conn.close()

    # Flash a success message
    flash("Form submitted successfully!", "success")
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
