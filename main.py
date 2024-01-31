from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# load user data  - For Login
def load_user_data():
    if os.path.exists('data.json'):
        with open('data.json', 'r') as file:
            return json.load(file)
    else:
        return {}

# save user data - For Register
def save_user_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

# home route
@app.route('/')
def home():
    return render_template('index.html')

# regiter route
@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        users = load_user_data()
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if username not in users:
            users[username] = {'email': email, 'password': password}
            save_user_data(users)
            return redirect(url_for('login'))
        else:
            error = "Username already exists!"
    return render_template('register.html', error=error)


# login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        users = load_user_data()
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            return "Login successful!"
        error = "Invalid email or password!"
    else:
        error: None
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
