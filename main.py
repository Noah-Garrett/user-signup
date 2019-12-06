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
    password_type_error=''

    if request.method=='GET':
        return render_template('main_form.html')
    else:
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        email = request.form['email']

        something_wrong=False

        #blank checks $$$
        if username == '':
            username_error='please enter a username'
            something_wrong=True
        if password == '':
            password_error='please enter a password'
            something_wrong=True
        if confirm_password == '':
            password_match='please confirm password'
            something_wrong=True

        #fancy boi checks 
        if len(username) <3 and len(username)>0 or len(username)>20 or ' ' in username:
            username_error='username cannot have space or less than 3'
            something_wrong=True

        if len(password) <3 and len(password)>0 or len(password)>20 or ' ' in password:
            password_type_error='passwords cannot contain spaces or be less than 3'
            something_wrong=True
        
        if password != confirm_password:
            password_match="passwords do not match"
            something_wrong=True

        #email oh lawd
        if email != '':
            if '@'  not in email or  '.'  not in email:
                email_error='please enter a valid email'
                something_wrong=True

         #if it's all good you're clear
        if something_wrong==False:
            return redirect('/success?user=' + username)

        return render_template("main_form.html",username_error = username_error,password_error = password_error,password_match= password_match,email_error=email_error, email=email, username=username, password_type_error=password_type_error)
    
@app.route('/success')
def success():
    username=request.args.get('user')
    return render_template("logged_in.html", username=username)


app.run()