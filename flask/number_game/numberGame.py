from flask import Flask, render_template, request, redirect, session
import os, random


app = Flask(__name__)

app.secret_key = os.urandom(24) # you need to set a secret key for security purposes
# routing rules and rest of server.py below
# print "appsecretkey=", app.secret_key 

@app.route('/')
def index():
	if 'r_number' not in session:
		session['r_number']=random.randrange(0,101)
		session['guess']="wrong"
		session['guessedNo']=int(0)

	return render_template("index.html", number=session['guessedNo'])

@app.route('/guess', methods=['POST'])
def guess():
	guess=int(request.form['u_guess'])	
	if (guess > int(session['r_number'])):
		session['guess']="high"
	elif (guess < int(session['r_number'])):
		session['guess']="low"	
	elif (guess == int(session['r_number'])):
		session['guess']="correct"	
	session['guessedNo']=guess	
	# print "random number: ", session['r_number']
	# print "guess=", guess, session['guess']
	return redirect ('/')

@app.route('/again', methods=['POST'])
def reset():
	print "OK again"
	session['r_number']=random.randrange(0,101)
	session['guess']="wrong"
	# print "random number: ", session['r_number']
	# print "guess=", guess, session['guess']
	return redirect ('/')

app.run(debug=True) # run our server
