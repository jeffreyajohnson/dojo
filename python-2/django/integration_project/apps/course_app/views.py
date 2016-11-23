from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.db.models import Count
from .models import Course 
from ..login_reg_app.models import User


# Create your views here.
def index(request):
    courses = Course.objects.all()
    # print "courses:", courses

    # print ("query:", 50*"*")
    # print courses.query
    # print ("object:",50*"*")
    # print courses
    # print (50*"*")
    # for course in courses:
    #     print course.name, course.description

    context = {
        'courses': courses
    }
    return render(request, 'course_app/index.html', context)


def add_course(request):
    if request.method == "POST":
        print "Got add post" 
        course_number = request.POST['catalogNo']
        course_name = request.POST['name']
        course_description = request.POST['description']
        print course_name   
        print course_description
        Course.objects.create(catalogNo=course_number, name=course_name, description=course_description)
    return redirect (reverse('courses:index'))


def delete_course(request, id):
    print "Got delete request" 
    courses = Course.objects.filter(id=id)
    
    print ("query:", 50*"*")
    print courses.query
    print ("object:",50*"*")
    print courses
    print (50*"*")
    for course in courses:
        print course.name, course.description

    context = {
        'courses': courses
    }

    return render(request, 'course_app/verify.html', context)

       
def delete(request, id, verification):
    print "Got delete command"
    print verification 
    if verification == "confirm":
        Course.objects.filter(id=id).delete()
    return redirect (reverse('courses:index'))

def enroll(request):
    print "In enroll method"
    courses = Course.objects.annotate(num_users = Count('users'))
    users = User.objects.all()
    context = {
        'courses': courses,
        'users': users
    }

    return render(request, 'course_app/enroll.html', context)


def enroll_user(request):
    error=False
    print "request.POST['user_id']", request.POST['user_id']
    print "request.POST['course_id']", request.POST['course_id']

    if request.POST['course_id']=="Courses":
        messages.add_message(request, messages.INFO,"You need to select a course")
        error=True
    if request.POST['user_id']=="Users":
        messages.add_message(request, messages.INFO,"You need to select a user")
        error=True

    if not error:
        try:
            this_enrollment = Course.objects.get(id=request.POST['course_id'], users=request.POST['user_id'])
        except Course.DoesNotExist:
            this_enrollment = Course.objects.get(id=request.POST['course_id'])
            this_enrollment.users.add(request.POST['user_id'])
            print"Added user_id:{} to course_id{}".format(request.POST['user_id'], request.POST['course_id']) 
            return redirect (reverse('courses:enroll'))
        else:
            this_course = Course.objects.filter(id=request.POST['course_id']).values()
            this_user = User.objects.filter(id=request.POST['user_id']).values()    
            print"this_enrollment", this_course[0]
            messages.add_message(request, messages.INFO, "{} {} is already signed up for {}".format(this_user[0]['first_name'], this_user[0]['last_name'], this_course[0]['name']) )
            return redirect (reverse('courses:enroll'))
    else:
        messages.add_message(request, messages.INFO, "Please try again")
        print"we got error messages"
        return redirect (reverse('courses:enroll'))
            

    
   
