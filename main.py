from flask import Flask, request, redirect, render_template
import html
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("main_form.html", username_error='',password_error='',password_match='', email_error='')


@app.route('/', methods=['POST'])
def error():
    username_error=''
    password_error=''
    password_match=''
    email_error=''
    
    username = request.form['username']

    if username == '':
        username_error='please enter a username'
    #elif password == '':
        #password_error='please enter a password'
    #elif confirm_password == '':
        #password_match='please confirm password'

    if len(username) <=3 and len(username)>0:
        username_error='that username is too short'

    return render_template("main_form.html",username_error = username_error,password_error = password_error,password_match= password_match,email_error=email_error)
    


app.run()