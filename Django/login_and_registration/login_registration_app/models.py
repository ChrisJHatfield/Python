from django.db import models
from datetime import date, datetime
import re
import bcrypt

class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        #first_name
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First Name should be at least 2 characters"
        #last_name
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last Name should be at least 2 characters"
        #email
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        user = User.objects.filter(email=postData['email'])
        if user:
            errors['email'] = "Email already exists"
        #birthdate
            #validate entry in field
            #validate birthday is in the past
        date_today_in_seconds = datetime.now().timestamp()
        user_birthdate = datetime.strptime(postData['birthdate'], '%Y-%m-%d').timestamp()
        if user_birthdate > date_today_in_seconds:
            errors['birthdate_future'] = "Birthdate should be in the past"
            #validate user is 13 years of age
        thirteen_years_in_seconds = 13 * 365 * 24 * 60 * 60
        if user_birthdate > (date_today_in_seconds - thirteen_years_in_seconds):
            errors['birthdate_thirteen'] = "Must be at least 13 years old to register"
        #password
        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"
        elif postData['password'] != postData['confirm_password']:
            errors['password'] = "Passwords do not match"
        #confirm password
        if len(postData['confirm_password']) < 8:
            errors['confirm_password'] = "Confirm PW should be at least 8 characters"
        return errors

    def login_validator(self, postData):
        errors = {}
        #email
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        
        #password
        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"
        user_list = User.objects.filter(email=postData['email'])
        if len(user_list) == 1:
            if bcrypt.checkpw(postData['password'].encode(), user_list[0].password.encode()):
                print("password match")
            else:
                print("failed password")
                errors['password_login'] = "Does not match"
        else:
            errors['email_login'] = "Does not exist"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    birthdate = models.DateField()
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()