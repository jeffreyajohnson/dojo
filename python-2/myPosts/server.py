from flask import Flask, render_template, redirect, request, flash, session
from flask_bcrypt import Bcrypt
from mysqlconnection import MySQLConnector
import os, random, re

app = Flask(__name__)
app.secret_key = os.urandom(24)


bcrypt = Bcrypt(app)
mysql=MySQLConnector(app, 'MyPosts')

@app.route('/')
def index():
	return redirect('/posts')


@app.route('/posts')
def posts():
	print"into posts"
	
	query = "SELECT * FROM posts"
	posts = mysql.query_db(query) 

	return render_template("posts.html", posts=posts)

@app.route('/post/new', methods=['POST'])
def new_post():
	print "new post received:", request.form['new_post']

	#AJAX change - remove data since this is now passed in via html $.post method 
	# data={ 'post': request.form['new_post'] } 

	#AJAX change - use format method to insert data into query string
	query = "INSERT INTO myposts.posts (description, created_at, updated_at) VALUES ('{}', NOW(), NOW())".format(request.form['new_post'])
	#AJAX change - remove data from db call
	mysql.query_db(query)

	#AJAX change (two new lines + modified return) - update query and send to partials
	updated_query="SELECT * FROM posts"
	posts = mysql.query_db(updated_query) 
	print "posts= ", posts
	print("query return:", mysql.query_db(updated_query))
	print "calling partial"
	return render_template('partials/posts.html', posts=posts)  #AJAX change - send to partials with data

app.run(debug=True)

