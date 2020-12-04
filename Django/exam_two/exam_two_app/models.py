from django.db import models
import re
import bcrypt

#User Models******************************************************************************
class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        #first_name
        if len(postData['register_first_name']) < 2:
            errors['register_first_name'] = "First Name should be at least 2 characters"
        #last_name
        if len(postData['register_last_name']) < 2:
            errors['register_last_name'] = "Last Name should be at least 2 characters"
        #email
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['register_email']):
            errors['register_email'] = "Invalid email address!"
        user = User.objects.filter(email=postData['register_email'])
        if user:
            errors['register_email'] = "Email already exists"
        #password
        if len(postData['register_password']) < 8:
            errors['register_password'] = "Password should be at least 8 characters"
        elif postData['register_password'] != postData['register_confirm_password']:
            errors['password'] = "Passwords do not match"
        #confirm password
        if len(postData['register_confirm_password']) < 8:
            errors['register_confirm_password'] = "Confirm PW should be at least 8 characters"
        return errors

    def login_validator(self, postData):
        errors = {}
        #email
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['login_email']):
            errors['login_email'] = "Invalid email address!"
        #password
        user_list = User.objects.filter(email=postData['login_email'])
        if len(user_list) == 1:
            if bcrypt.checkpw(postData['login_password'].encode(), user_list[0].password.encode()):
                print("password match")
            else:
                errors['login_password'] = "Does not match"
        else:
            errors['login_email'] = "Does not exist"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=60)
    #wisher -> 1 to Many
    wishes_liked = models.ManyToManyField('Wish', related_name="users_who_liked")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class WishManager(models.Manager):
    def wish_validator(self, postData):
        errors = {}
        #item
        if len(postData['wish_item']) < 3:
                errors['wish_item'] = "A Wish should be at least 3 characters"
        #description
        if len(postData['wish_description']) < 3:
                errors['wish_description'] = "Wish description should be at least 3 characters"
        return errors

class Wish(models.Model):
    item = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    wish = models.ForeignKey(User, related_name="wisher", on_delete=models.CASCADE)
    granted_wish = models.IntegerField(default=0)
    #users_who_liked -> Many to Many
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = WishManager()