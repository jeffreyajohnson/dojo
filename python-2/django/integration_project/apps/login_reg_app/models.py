from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import bcrypt, re

# Create your models here.
class UserManager(models.Manager):

    def validate_registration(self, *args):
        print"in validate_registration"
        print"*********"
        print "args:", args
        print"*********"
        first_name=args[0]['ufname']
        last_name=args[0]['ulname']
        email=args[0]['uemail']
        password=args[0]['password']
        confirm_pwd=args[0]['confirm_pwd']

        print("variables:", first_name, last_name, email, password, confirm_pwd)
        
        errors=[]
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

        if not email:
            errors.append("Email cannot be blank!")
        elif not EMAIL_REGEX.match(email):
            errors.append("Invalid Email Address!")

        if not first_name:
            errors.append("Need to include first name")
        if not last_name:
            errors.append("Need to include last name")      
        if  re.search(r"\d", first_name) or re.search(r"\d", last_name):
            errors.append("Names cannot contain numerals")  
        if not email:
            errors.append("Email cannot be blank!")
        elif not EMAIL_REGEX.match(email):
            errors.append("Invalid Email Address!")
        if not password:
            errors.append("Need to include password")  
        if not confirm_pwd:
            errors.append("Please confirm password")    
        if (len(password) >0 and len(confirm_pwd) >0):
            if password != confirm_pwd:
                errors.append("Password and Confirmation Password does not match") 
            if len(password) < 8:
                 errors.append("Passwords need to contain at least 8 characters") 

        try:
            user = User.objects.get(email=email)
        except ObjectDoesNotExist: 
            pass
        else:
            errors.append("User with that email ({}) already exists in our database".format(email))
            return(False, errors) 

        if not errors:
            pw_hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            print{"********pw_hashed********"}
            print(pw_hashed)
            user = User(first_name=first_name, last_name=last_name, email=email, pw_hash=pw_hashed)
            user.save()
            user = User.objects.filter(email=email).values() # .values() returns dictionary of elements in list[0]
                        
            # for debug
            users= User.objects.all()
            print("query return:", users)
            for user in users:
              print(user)
            # end for debug

            return(True, user)
        else:
            return(False, errors) 

    def validate_login(self, *args):
        errors=[]
        print"in validate_login"
        print"*********"
        print "args:", args
        print"*********"   
        email=args[0]['user_email']
        password=args[0]['password']
        try:
            # user = User.objects.get(email=email).values()
            user = User.objects.filter(email=email).values()
            print"try query return for {}:{}".format(email, user)
        except ObjectDoesNotExist:
            errors.append("No such user ({}) exists in our database".format(email))
            print "No such user ({}) exists in our database".format(email)
            return(False, errors) 
               
        if bcrypt.hashpw(password.encode(), user[0]['pw_hash'].encode()) == user[0]['pw_hash'].encode():
            print("It Matches!")
            return(True, user[0]['first_name'], user[0]['id'])
        else:
            print("Password Does not Match")
            errors.append("Login failed")
            return(False, errors)  
        

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
