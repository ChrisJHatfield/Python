from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Book
import bcrypt

#Render Page Functions*****************************
def home(request):
    return render(request, 'home.html')

def books(request):
    if 'uuid' not in request.session:
        return redirect('/')
    context = {
        'user_in_session' : User.objects.get(id=request.session['uuid'])
    }
    return render(request, 'books.html', context)

#User Functions************************************
def register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')
    else:
        print(request.POST)
        password = request.POST['register_password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            first_name = request.POST['register_first_name'],
            last_name = request.POST['register_last_name'],
            email = request.POST['register_email'],
            password = pw_hash,
        )
    request.session['uuid'] = user.id
    return redirect('/books')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
    else:
        print(request.POST)
        user = User.objects.get(email=request.POST['login_email'])
        if user:
            logged_user = user
            if bcrypt.checkpw(request.POST['login_password'].encode(), logged_user.password.encode()):
                request.session['uuid'] = logged_user.id
                return redirect('/books')
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

#Book Functions************************************
def add_favorite_book(request):
    print(request.POST)
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
    else:
        user_id = User.objects.get(id=request.session['uuid'])
        Book.objects.create(
        title = request.POST['book_title'],
        description = request.POST['book_description'],
        uploaded_by = user_id,
        )
        book_uploaded = User.objects.first().books_uploaded.all()
        print(book_uploaded)
        user_id.liked_books.add(book_uploaded)
    return redirect('/books')