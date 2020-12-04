from django.db import models
from datetime import date, datetime
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
    #user_messages (1 -> Many)
    #comments (1 -> Many)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

#Message Models******************************************************************************
class MessageManager(models.Manager):
    def message_validator(self, postData):
        errors = {}
        if len(postData['posted_message']) < 2:
            errors['posted_message'] = "Message should be at least 2 characters"
        return errors

class Message(models.Model):
    post = models.CharField(max_length=255)
    user_message = models.ForeignKey(User, related_name="user_messages", on_delete=models.CASCADE)
    #comments = (1 -> Many)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()

#Comment Models******************************************************************************
class CommentManager(models.Manager):
    def comment_validator(self, postData):
        errors = {}
        if len(postData['posted_comment']) < 2:
            errors['posted_comment'] = "Comment should be at least 2 characters"
        return errors

class Comment(models.Model):
    text = models.CharField(max_length=255)
    commenter = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    message_on_comment = models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()