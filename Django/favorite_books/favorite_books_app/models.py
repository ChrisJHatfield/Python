from django.db import models
import re
import bcrypt

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
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    password = models.CharField(max_length=255)
    #books_uploaded  (One -> Many)
    #liked_books  (Many <--> Many)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        #title
        if len(postData['book_title']) < 0:
            errors['book_title'] = "Book title is required"
        #description
        if len(postData['book_description']) < 5:
            errors['book_description'] = "Description must be at least 5 characters"
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=510)
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()