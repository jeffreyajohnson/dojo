from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
import os, random
import datetime


activities=[]

def index(request):
	if 'gold' not in request.session:
		request.session['gold']=0
		request.session['activities']=""
	return render(request, 'ninjaGold/index.html')

def process_money(request):
	if request.method == "POST":
		print "Got post"
		now= datetime.datetime.now()
		date = str(now.strftime('(%m/%d/%y at %I:%M:%S %p)'))
		if (request.POST['building'] == "farm"):
			delta=random.randrange(10,21) #farm
			request.session['gold']+= delta
			activity = {
				'results': "Earned "+str(delta)+" golds from the farm!",
				'date': date
			}
		elif (request.POST['building'] == "cave"):
			delta=random.randrange(5,11) #cave
			request.session['gold']+= delta
			activity = {
				'results': "Earned "+str(delta)+" golds from the cave!",
				'date': date
			}	
		elif (request.POST['building'] == "house"):
			delta=random.randrange(2,6) #house
			request.session['gold']+= delta
			activity = {
				'results': "Earned "+str(delta)+" golds from the house!",
				'date': date
			}	
		elif (request.POST['building'] == "casino"):
			delta=random.randrange(-50,51) #casino
			request.session['gold']+= delta
			if (delta < 0):
				activity = {
					'results': "Lost "+str(delta)+" golds to the casino!",
					'date': date
				}	
			else:
				activity = {
				'results': "Earned "+str(delta)+" golds from the casino!",
				'date': date
				}	
		activities.insert(0, activity)
		request.session['activities']=activities	
		print activities
		return redirect (reverse('ninja-gold:index'))





















	