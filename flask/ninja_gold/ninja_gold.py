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
	
	return render_template("index.html", amt_gold=session['gold'], activities=activities)

@app.route('/process_money', methods=['POST'])
def process_money():
	if (request.form['building'] == "farm"):
		delta=random.randrange(10,21) #farm
		session['gold']+= delta
		activity = {
			'results': "Earned "+str(delta)+" golds from the farm!",
			'date': datetime.datetime.now()
		}
	elif (request.form['building'] == "cave"):
		delta=random.randrange(5,11) #cave
		session['gold']+= delta
		activity = {
			'results': "Earned "+str(delta)+" golds from the cave!",
			'date': datetime.datetime.now()
		}	
	elif (request.form['building'] == "house"):
		delta=random.randrange(2,6) #house
		session['gold']+= delta
		activity = {
			'results': "Earned "+str(delta)+" golds from the house!",
			'date': datetime.datetime.now()
		}	
	elif (request.form['building'] == "casino"):
		delta=random.randrange(-50,51) #casino
		session['gold']+= delta
		if (delta < 0):
			activity = {
				'results': "Lost "+str(delta)+" golds to the casino!",
				'date': datetime.datetime.now()
			}	
		else:
			activity = {
			'results': "Earned "+str(delta)+" golds from the casino!",
			'date': datetime.datetime.now()
			}	

	activities.append(activity)	
	# print activities
	return redirect ('/')

app.run(debug=True) # run our server
