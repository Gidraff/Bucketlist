"""modules and packages to be imported"""
from flask import Flask, request, redirect, render_template, url_for
from app.main.user import User

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/ask')
def ask():
    return render_template('ask.html')

@app.route('/createbl')
def createbl():
    return render_template('createbl.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password =request.form['password']
    new_user = User(username,email,password)
    new_user.register_user(username,email,password)

    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = None
    if request.form['username'] != username or\
     request.form['password'] != password:
        msg= 'Invalid credentials.please try again'
    else:
        return redirect(url_for('index'))
    return render_template('login.html', msg=msg)






if __name__ == '__main__':
    app.run()
    app.config.from_object('config')