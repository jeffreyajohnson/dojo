from flask import Flask, render_template, request, redirect, session
import os, random
import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24) 

activities=[]

@app.route('/')
def index():
	if 'gold' not in session:
		session['gold']=0
		session['activity']=""
		session['date']=""
		# session['index']=int(0)
		# print "gold=", session['gold']	
	
	return render_template("index.html", activities=activities)

@app.route('/process_money', methods=['POST'])
def process_money():
	if (request.form['building'] == "farm"):
		delta=random.randrange(10,21) #farm
		activity = {
			'results': "Earned "+str(delta)+" golds from the farm!",
			'date': datetime.datetime.now()
		}	
		print activity
	elif (request.form['building'] == "cave"):
		# session['gold']+=random.randrange(5,11) #cave
		delta=random.randrange(5,11) #cave
		session['gold']+= delta
		print"cave gold win=", delta
		print" gold amount =", session['gold']
	elif (request.form['building'] == "house"):
		# session['gold']+=random.randrange(2,6) #house
		delta=random.randrange(2,6) #house
		session['gold']+= delta
		print"house gold win=", delta
		print" gold amount =", session['gold']
	elif (request.form['building'] == "casino"):
		# session['gold']+=random.randrange(-50,51) #casino
		delta=random.randrange(-50,51) #casino
		session['gold']+= delta
		print"casino win/loss=", delta
		print" gold amount =", session['gold']

	activities.append(activity)	
	print activities
	return redirect ('/')


app.run(debug=True) # run our server
