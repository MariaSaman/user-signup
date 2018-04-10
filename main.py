from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/validate')
def index():
    template = jinja_env.get_template('user_form.html') 
    #username_error = request.args.get("error")
    return template.render()
   

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

#       IF email field filled in, must have 3-20 char no space, a single @ and a single .
#def valid_email(string)
#    if char in string == char.isalnum or

#def valid_email_field(email)
    

# each feedback message should be next to the field it refers to


@app.route('/validate', methods=['POST'])
def validate_user():
    username=request.form['user-name']
    password=request.form['password']
    verify_password=request.form['password-conf']
    email=request.form['email']

    username_error=''
    password_error=''
    password_conf_error=''
    email_error=''
    
    if not valid_char_count(username) or no_space_string(username):
        username_error = "That's not a valid username"
        username = ''
        
    if not valid_char_count(password) or no_space_string(password):
        password_error = "That's not a valid password"
        password = ''

    if not valid_char_count(verify_password) and valid_password_conf(password, verify_password):
        password_conf_error = "Passwords do not match"
        password_conf_error = ''
    
    if not username_error and not password_error and not password_conf_error:
        return redirect("/welcome")

    else:
        template = jinja_env.get_template('user_form.html')
        return template.render(username=username, password=password, verify_password=verify_password)    

    
# if input for username and email are valid, preserve what user typed

#display a welcome message of "Welcome [username]"

@app.route("/welcome-user", method=['POST'])
def welcome():
    user = request.form['user-name']
    template= request.form('user-name')
    return template.render(username-username)

app.run()



