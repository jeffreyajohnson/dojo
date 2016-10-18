from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninja/')
def ninja():
	return render_template('ninja.html')

@app.route('/ninja/<ninjacolor>/')
def show_ninja(ninjacolor):
	if ninjacolor == "blue":
		return render_template('blue.html')
	elif ninjacolor == "orange":
		return render_template('orange.html')
	elif ninjacolor == "red":
		return render_template('red.html')
	elif ninjacolor == "purple":
		return render_template('purple.html')
	else:
		return render_template('april.html')	

app.run(debug=True)