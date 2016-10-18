from flask import Flask, render_template, request, redirect, session, flash
import os, random, re

app = Flask(__name__)
app.secret_key = os.urandom(24)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
 

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/user', methods=['POST'])
def create_user():
    errors=[]
    print "Got Post Info"
    ufname = request.form['ufname']
    ulname = request.form['ulname']
    uemail = request.form['uemail']
    upwd = request.form['upwd']
    confirm_pwd = request.form['confirm_pwd']
     
    if len(ufname) <1:
        errors.append("Please enter first name")
    if len(ulname) <1:
        errors.append("Please enter last name")      
    if  re.search(r"\d", ufname) or re.search(r"\d", ulname):
        errors.append("Names cannot contain numerals")  
    if len(uemail) <1:
        errors.append("Please enter email")
    elif not EMAIL_REGEX.match(uemail):
        errors.append("Please enter valid email")
    if len(upwd) <1:
        errors.append("Please enter password")  
    if len(confirm_pwd) <1:
        errors.append("Please confirm password")    
    if (len(upwd) >1 and len(confirm_pwd) >1):
        print"comparing passwords"
        if upwd != confirm_pwd:
            errors.append("Passwords do not match") 
        if len(upwd) < 8:
             errors.append("Passwords need to contain at least 8 characters") 

    if errors:
        for error in errors:
            flash(error)        
    else:
        flash("Thanks for submitting your information.")
    
    return redirect ('/')

# @app.route('/index', methods=['GET'])
# def return2main(): 
# 	print "Got Return Request"
# 	return render_template("index.html")
   
app.run(debug=True) # run our server
