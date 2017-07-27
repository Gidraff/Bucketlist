"""modules and packages to be imported"""
from flask import Flask, request, redirect, render_template, url_for, flash, session
from main.user import User
from main.data import Data


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    """renders the index page"""
    return render_template('index.html')

@app.route('/about')
def about():
    """renders the about page"""
    return render_template('about.html')

@app.route('/ask')
def ask():
    """renders the ask page"""
    return render_template('ask.html')

@app.route('/createbl', methods=['GET','POST'])
def createbl():
    """renders the createbl page"""
    title = request.form.get('title')
    description = request.form.get('description')
    if request.method == 'POST':
        for user in Data.users:
            if user['email'] == session['user_email']:
                user_ = User(user['username'],
                             user['email'], 
                             user['password'], 
                             user['id'])

                user_.create_bucketlist(title, description)
        return redirect(url_for('dashboard'))
    return render_template('createbl.html')

@app.route('/dashboard')
def dashboard():
    """renders dashboard dashboard html"""
    current_user = None
    for user in Data.users:
        if user['email'] == session['user_email']:
            current_user = user
    bucketlists = Data.retrieve_data(current_user['id'])
    return render_template('dashboard.html', bucketlists = bucketlists)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """register users information"""
    username = request.form.get('username')
    email = request.form.get('email')
    password =request.form.get('password')
    if request.method == 'POST':
        if User.register_user(username,email,password):
             return redirect(url_for('login'))
    else:
        return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """verifies and login user """
    if request.method == 'POST':
        user_email = request.form.get('user_email')
        password = request.form.get('user_password')
        for user in Data.users:
            if user['email'] == user_email and user['password'] == password:
                print(Data.users)  
                session['user_email'] = user_email
                return redirect(url_for('createbl'))
        flash('Invalid credentials')
    return render_template('login.html')

if __name__ == '__main__':
    app.secret_key="secretkey4321"
    app.run(debug=True)
