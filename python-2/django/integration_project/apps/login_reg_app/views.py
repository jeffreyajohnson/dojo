from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
  return render(request, "login_reg_app/index.html")

def process(request):
    print"in process method"
    if request.method=='POST':
        print"got method=post"
        print(request.POST)
        response = User.objects.validate_registration(request.POST)
        print("response", response)
        if response[0]:
            print "Register success!!"
            
            context = {
                'first_name': request.POST['ufname'],
                'path': "registered"
            }
            print("context:", context)            
            return render(request, 'login_reg_app/success.html', context)
        else:
            context = {
                'errors': response[1]
            }
            for error in response[1]:
                print"error in response:", error
            return render(request, 'login_reg_app/index.html', context)
    else:
        return render(request, 'login_reg_app/index.html')

def login(request):
    print"in login method"
    if request.method=='POST':
        print"got method=post"
        print(request.POST)
        response = User.objects.validate_login(request.POST)
        print("response", response)
        if response[0]:
            print "Login success!!"
            request.session['id']= response[2]
            print"request.session['id']:", request.session['id'] 
            context = {
                'first_name': response[1],
                'path': "logged in"
            }
            print("context:", context)            
            return render(request, 'login_reg_app/success.html', context)
        else:
            context = {
                'errors': response[1]
            }
            for error in response[1]:
                print"error in response:", error
            return render(request, 'login_reg_app/index.html', context)
    else:
        return render(request, 'login_reg_app/index.html')

def manage_user(request):
    print "Got manage request" 
    users=User.objects.all()
    print ("query:", 50*"*")
    print users.query
    print ("object:",50*"*")
    print users
    print (50*"*")
    for user in users:
        print user.first_name, user.last_name

    context = {
        'users': users
    }

    return render(request, 'login_reg_app/manage.html', context)

def delete_user(request, id):
    print "Got delete request" 
    User.objects.filter(id=id).delete()
    users=User.objects.all()
    print ("query:", 50*"*")
    print users.query
    print ("object:",50*"*")
    print users
    print (50*"*")
    for user in users:
        print user.first_name, user.last_name

    context = {
        'users': users
    }

    return render(request, 'login_reg_app/manage.html', context)

       


