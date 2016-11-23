from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
# import random 
# from random_words import RandomWords
# rw=RandomWords()

from django.utils.crypto import get_random_string

# Create your views here.
def index(request):	
	return redirect(reverse('random-word:create'))
	

def create_random_number(request):
	print("request.method: ", request.method)
	if request.method == "POST":
		print request.POST
		request.session['count'] = request.session['count'] + 1
		# number = random.randrange(1, 10**14)
		# request.session['number'] = random.randrange(1, 10**14)
		request.session['word'] = get_random_string(length=14)

		print ('*'*50)
		print("random word:", request.session['word'])
		print ('*'*50)		
		
	else:
		request.session['count']=0
		request.session['word']='(Need to run random word generator)'

	print"count: ", request.session['count']

	return render(request, 'randomWord/index.html')


