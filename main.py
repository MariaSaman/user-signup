from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index(): 
    #username_error = request.args.get("error")
    return render_template("user_form.html")
   

#validation( reject and re-render form with feedback) 
#   validation criteria: 
#       fields 1-3 cannot be left empty
#       username and password cannot contain space character, ex: be less than 3 or more than 20 char

def valid_char_count(string):
    if len(string) <= 20 and len(string) >= 3:
        return True
    else:
        return False

def no_space_string(string):
    if " " not in string: 
        return True
    else:
        return False 

#       password and password confrimation do not match

def valid_password_conf(password, password_conf):
    if password == password_conf:
        return True
    else:
        return False

#   IF email field filled in, must have 3-20 char no space, a single @ and a single .
#   def valid_email(string)
#   if char in string == char.isalnum or

def valid_email(email):
    if email == '':
        return True
    else:
        if email.count('@') == 1 and email.count('.') == 1 and valid_char_count(email) and no_space_string(email):
            return True
        else: 
            return False
    

# each feedback message should be next to the field it refers to


@app.route('/', methods=['POST'])
def validate_user():
    username=request.form['user-name']
    password=request.form['password']
    verify_password=request.form['password-conf']
    email=request.form['email']

    username_error=''
    password_error=''
    password_conf_error=''
    email_error=''
    
    if not valid_char_count(username) or not no_space_string(username):
        username_error = "That's not a valid username"
        username= ''
        
    if not valid_char_count(password) or not no_space_string(password):
        password_error = "That's not a valid password"

    if not valid_char_count(verify_password) or not valid_password_conf(password, verify_password):
        password_conf_error = "Passwords do not match"

    if not valid_email(email):
        email_error = "That's not a valid email"
        email = ''
    
    if not username_error and not password_error and not password_conf_error and not email_error:
        return redirect("/welcome?user=" + username)

    else:
        return render_template("user_form.html",
                                username=username,
                                email=email,
                                username_error=username_error,
                                password_error=password_error,
                                password_conf_error=password_conf_error,
                                email_error=email_error)    

    
# if input for username and email are valid, preserve what user typed

#display a welcome message of "Welcome [username]"

@app.route("/welcome")
def welcome():
    user = request.args.get('user')
    return render_template("welcome.html", username=user)

app.run()



