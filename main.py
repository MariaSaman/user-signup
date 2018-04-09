from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    template = jinja_env.get_template('user_form.html')
    return template.render()

#validation( reject and re-render form with feedback) 
#   validation criteria: 
#       fields 1-3 cannot be left empty


def required_field(string):
    if len(string) > 0:
        return True

#       username and password cannot contain space character, ex: be less than 3 or more than 20 char

def valid_char_count(string):
    if len(string) <= 20 and len(string) >= 3:
        return True
    else:
        return False

def no_space_string(string):
    if char in string !=' ':
        return True
    else:
        return False 

#       password and password confrimation do not match

def valid_password_conf(password, password_conf):
    if password == password_conf:
        return True
    else:
        return False

#       IF email field filled in, must have 3-20 char no space, a single @ and a single .
#def valid_email(string)
#    if char in string == char.isalnum or


# each feedback message should be next to the field it refers to


@app.route('/', methods=['POST'])
def validate_user():
    username=request.form['user-name']
    
    if user-name is not required_field(string) or user-name is not valid_char_count(string) or user-name is not no_space_string(string):
        error = "That's not a valid username"
        return redirect("/?error=" + error)

    password=request.form['password']
    verify_passowrd=request.form['password-conf']
    email=request.email['email']

username_error=''
#password_error=''
#password_conf_error=''
#email_error=''



    
# if input for username and email are valid, preserve what user typed

##display a welcome message of "Welcome [username]"

#@app.route("/welcome-user", method=['POST'])
#def welcome():
#    user = request.form['user-name']
#    template= request.form('user-name')
#    return template.render()

app.run()



