from django.shortcuts import render, HttpResponse
import datetime


# Create your views here.
def index(request):
	now = datetime.datetime.now()
	date = now.strftime("%b %d, %Y")
	clock=now.strftime("%I:%M %p")
	time = {
	"date": date,
	"clock": clock
	} 
	
	print ("time:" )
	return render(request, 'timedisplay/index.html', time)


