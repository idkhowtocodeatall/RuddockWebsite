from flask import Flask, request, session, g, redirect, url_for, abort, \
        render_template, flash
from sqlalchemy import create_engine, MetaData
import config, auth

app = Flask(__name__)
app.debug = True
app.secret_key = config.SECRET_KEY

""" Connect to the mySQL database. """
engine = create_engine(config.DB_URI, convert_unicode=True)
connection = engine.connect()

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  """ Procedure to process the login page. Also handles authentication. """
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']

    if auth.authenticate(username, password, connection):
      session['username'] = request.form['username']
      return redirect(url_for('home'))
    else:
      return render_template('login.html', msg='Incorrect username or ' + \
              ' password. Please try again!')

  return render_template('login.html')

@app.route('/logout')
def logout():
  session.pop('username', None)
  return redirect(url_for('home'))

@app.route('/users')
def show_users():
  """ Procedure to show a list of all users, with all membership details. """
  return render_template('userlist.html')

@app.route('/users/view/<username>')
def show_user_profile():
  """ Procedure to show a user's profile and membership details. """
  return render_template('view_user.html')

@app.route('/government')
def show_gov():
  return render_template('government.html')

@app.route('/about_us')
def show_about_us():
  return render_template('about_us.html')

@app.route('/news')
def show_news():
  return render_template('news.html')

@app.route('/calendar')
def show_calendar():
  return render_template('calendar.html')

if __name__ == "__main__":
  app.debug = True
  app.run()
