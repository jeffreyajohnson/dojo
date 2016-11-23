from flask import Flask, render_template, redirect, request, flash, session
from flask_bcrypt import Bcrypt
from mysqlconnection import MySQLConnector
import os, random, re

app = Flask(__name__)
app.secret_key = os.urandom(24)


bcrypt = Bcrypt(app)
mysql=MySQLConnector(app, 'ajax_notes_db')

@app.route('/')
def index():
	return redirect('/notes')


@app.route('/notes')
def notes():
	print"into  notes"
	
	query = "SELECT * FROM notes "
	notes = mysql.query_db(query) 

	return render_template("notes.html", notes=notes)

@app.route('/notes/new', methods=['POST'])
def new_note():
	print "new note received:", request.form['new_note']
	data={
		'title': request.form['note_title'],
		'description': request.form['new_note']
		}
	query = "INSERT INTO notes (title, description, created_at, updated_at) VALUES (:title, :description, NOW(), NOW())"
	mysql.query_db(query, data)

	return redirect ('/notes')

@app.route('/notes/<id>/delete')
def notes_delete(id):
	print"into notes delete"
	
	query = "DELETE FROM notes WHERE id={}".format(id)
	mysql.query_db(query) 

	query = "SELECT * FROM notes "
	notes = mysql.query_db(query)

	return render_template("notes.html", notes=notes)

@app.route('/notes/title/<id>/edit', methods=['POST'])
def notes_title_edit(id):
	print"into notes edit title"
	print(request.form['note_title'])

	data={
		'title': request.form['note_title'],
		}
	
	query= "UPDATE notes SET title = '{}' WHERE id={}".format(request.form['note_title'], id)
	print(query)
	mysql.query_db(query) 

	query = "SELECT * FROM notes "
	notes = mysql.query_db(query)

	return render_template("notes.html", notes=notes)

@app.route('/notes/<id>/edit', methods=['POST'])
def notes_edit(id):
	print"into edit note"
	print(request.form['revised_note'])

	query= "UPDATE notes SET description = '{}' WHERE id={}".format(request.form['revised_note'], id)
	print(query)
	mysql.query_db(query) 

	query = "SELECT * FROM notes "
	notes = mysql.query_db(query)

	return render_template("notes.html", notes=notes)

app.run(debug=True)

