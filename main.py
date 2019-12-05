from flask import Flask, request, redirect, render_template
import html
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/" ,methods=['POST','GET'])
def form():
    username_error=''
    password_error=''
    password_match=''
    email_error=''

    if request.method=='GET':
        return render_template('main_form.html')
    else:
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        email = request.form['email']

        something_wrong=True

        #blank checks $$$
        if username == '':
            username_error='please enter a username'
            something_wrong=False
        if password == '':
            password_error='please enter a password'
            something_wrong=False
        if confirm_password == '':
            password_match='please confirm password'
            something_wrong=False

        #fancy boi checks 
        if len(username) <=3 and len(username)>0 or len(username)>20 or ' ' in username:
            username_error='that username is is invalid'
            something_wrong=False
        
        if password != confirm_password:
            password_match="passwords do not match"
            something_wrong=False

        #email oh lawd
        if email != '':
            if '@'  not in email or  '.'  not in email:
                email_error='please enter a valid email'
                something_wrong=False

         #if it's all good you're clear
        if something_wrong==True:
            return redirect('/success?user=' + username)

        return render_template("main_form.html",username_error = username_error,password_error = password_error,password_match= password_match,email_error=email_error, email=email, username=username)
    
@app.route('/success')
def success():
    username=request.args.get('user')
    return render_template("logged_in.html", username=username)


app.run()