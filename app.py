# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session, abort
import os, math, requests
# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def welcome():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return redirect(url_for('home'))

# Route for handling the login page logic
@app.route('/home')
def home():
    # posts
    # user = User.query.filter_by(username=username).first_or_404()
    # posts = [
    #     {'author': user, 'body': 'Test post #1'},
    #     {'author': user, 'body': 'Test post #2'}
    # ]
    # return render_template('home.html', user = user, posts = posts)
    return render_template('home.html', user="Sam")

# for debug or demo, email = admin@gmail.com, password = admin
# use the next commented-out section if AWS credential is valid
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] != 'admin@gmail.com' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         r = requests.post('http://localhost:3000/users/create', data={"email": email, "password": password})
#         userId = r.text
#         print(userId)
#         if userId is None:
#             error = 'Invalid Credentials. Please try again.'
#         else:
#             session['logged_in'] = True
#             return redirect(url_for('home'))
#     return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return welcome()

@app.route('/register')
def register():
    return render_template('register.html')

# start the server with the 'run()' method
if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)