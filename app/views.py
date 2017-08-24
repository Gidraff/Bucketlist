"""modules and packages to be imported"""
from flask import Flask, request, redirect, render_template, url_for, flash, session
from wtforms import Form, StringField, PasswordField, TextField, validators
from functools import  wraps
from main.user import User

users = []


app = Flask(__name__)

class RegisterForm(Form):
    username = StringField('Username', [validators.Length(min=1, max=50)])
    email = TextField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('password', [
        validators.DataRequired(), validators.EqualTo('confirm', message='password do not match'), validators.Length(min=6, max=25)])
    confirm = PasswordField('confirm password')

@app.route('/')
@app.route('/index')
def index():
    """renders the index page"""
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """register users information"""
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        user = User(form.username.data, form.email.data, form.password.data)
        users.append(user)
        return redirect(url_for('createbl'))
    return render_template('register.html', form=form)

class LoginForm(Form):
    email = TextField('Email address', [validators.DataRequired(), validators.Email()])
    password = PasswordField('password', [
        validators.DataRequired(), validators.Length(min=6, max=25)
    ])

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login')
            return redirect(url_for('login', next=request.url))
    return decorated_function

@app.route('/login', methods=['GET','POST'])
def login():
    """verifies and login user """
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        for user in users:
            if user.email == form.email.data and\
             user.password == form.password.data:
                session['logged_in'] = user.email
                return redirect(url_for('createbl'))
    return render_template('login.html', form=form)

class CreateBucketlist(Form):
    title = StringField('Title')
    description = StringField('Description')

@app.route('/createbl', methods=['GET', 'POST'])
@login_required
def createbl():
    """renders the createbl page"""
    if not session['logged_in']:
        return redirect(url_for('login'))
    form = CreateBucketlist(request.form)
    if request.method == 'POST' and form.validate():
        for user in users:
            if user.email == session['logged_in']:
                user.create_bucketlist(form.title.data, form.description.data)
                return redirect(url_for('dashboard'))
            else:
                return redirect(url_for('login'))
    return render_template('createbl.html', form=form)

@app.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    """renders dashboard dashboard html"""
    print("users>>",users, users[0].bucketlists , users[0].email , session['user_email'])
    for user in users:
        if user.email == session['logged_in']:
            bucketlists = user.bucketlists
            print("this is buck>>>",bucketlists)
            return render_template('dashboard.html', bucketlists=bucketlists)
    return redirect(url_for('login'))

@app.route('/delete_bucketlist/<id>', methods=['GET', 'POST'])
@login_required
def delete_bucketlist(id):
    for user in users:
        if user.email == session['logged_in']:
            user.delete_bucketlist(id)
            return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

class EditBucketlist(Form):
    title = StringField('new title')
    description = StringField('new description')

@app.route('/edit_bucketlist/<id>', methods=['GET', 'POST'])
@login_required
def edit_bucketlist(id):
    """edit user bucketlist"""
    form = EditBucketlist(request.form)
    if request.method == 'POST' and form.validate():
        for user in users:
            if user.email == session['logged_in']:
                user.update_bucketlist(id, form.title.data, form.description.data )
                return redirect(url_for('dashboard'))
    return render_template('edit_bucketlist.html', form=form)
    

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    """remove user email session if its there"""
    session.pop('logged_in', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.secret_key = "secretkey4321"
    app.run(debug=True)
