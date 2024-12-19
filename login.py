from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector
import hashlib

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="demo"
)
cursor = conn.cursor()

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Route to display the registration/login form
@app.route('/')
def index():
    return render_template('login.html')

# Route to handle user registration
@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    hashed_password = hash_password(password)
    
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, hashed_password))
        conn.commit()
        flash("Registration successful! Please log in.")
        return redirect(url_for('index'))
    except mysql.connector.IntegrityError:
        flash("Username already exists!")
        return redirect(url_for('index'))

# Route to handle user login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    hashed_password = hash_password(password)
    
    cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, hashed_password))
    user = cursor.fetchone()
    
    if user:
        session['username'] = username
        flash("Login successful!")
        return redirect(url_for('dashboard'))
    else:
        flash("Invalid username or password!")
        return redirect(url_for('index'))

# Route for the dashboard page after login
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f"Welcome, {session['username']}! You are logged in."
    else:
        return redirect(url_for('index'))

# Route to log out
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("You have been logged out.")
    return redirect(url_for('index'))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

# Close the database connection
cursor.close()
conn.close()
