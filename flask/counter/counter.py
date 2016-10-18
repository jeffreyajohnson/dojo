from flask import Flask, render_template, request, redirect, session
import os
app = Flask(__name__)

app.secret_key = os.urandom(24) # you need to set a secret key for security purposes
# routing rules and rest of server.py below
print "appsecretkey=", app.secret_key 

@app.route('/')
def index():
	try: 
		session['count']
	except:
		print "No count yet exists"
		session['count']=0
	session['count']+=1
	return render_template("index.html")

app.run(debug=True) # run our server
