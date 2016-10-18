from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/user', methods=['POST'])
def create_user():
    print "Got Post Info"
    uname = request.form['name'] 
    ulocation = request.form['location']
    ulanguage = request.form['language']
    ucomments = request.form['comment']
    print "uname:", uname, "uloaction;", ulocation, "ulanguage:", ulanguage, "ucomments", ucomments 
    return render_template('user.html', name=uname, location=ulocation, language=ulanguage, comment=ucomments)


@app.route('/index', methods=['GET'])
def return2main(): 
	print "Got Return Request"
	return render_template("index.html")
   
app.run(debug=True) # run our server
