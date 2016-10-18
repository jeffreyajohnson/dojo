from flask import Flask, render_template, request, redirect, session, flash
import os, random

app = Flask(__name__)

app.secret_key = os.urandom(24)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/user', methods=['POST'])
def create_user():
    errors=[]
    print "Got Post Info"
    uname = request.form['name'] 
    if len(uname) <1:
        errors.append("Please enter user name")
    ulocation = request.form['location']
    ulanguage = request.form['language']
    ucomments = request.form['comment']
    if len(ucomments) <1:
        errors.append("Please enter a comment")
    elif len(ucomments) > 120:
        errors.append("Sorry, please limit your comment to 120 characters.")    
    print "uname:", uname, "uloaction;", ulocation, "ulanguage:", ulanguage, "ucomments", ucomments 
    
    if errors:
        for error in errors:
            flash(error)
        return redirect ('/')
    else:
        return render_template('user.html', name=uname, location=ulocation, language=ulanguage, comment=ucomments)


@app.route('/index', methods=['GET'])
def return2main(): 
	print "Got Return Request"
	return render_template("index.html")
   
app.run(debug=True) # run our server
