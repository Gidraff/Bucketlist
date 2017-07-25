"""modules and packages to be imported"""
from flask import Flask, request, redirect, render_template, url_for

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

    return redirect(url_for('login'))







if __name__ == '__main__':
    app.run()
    app.config.from_object('config')