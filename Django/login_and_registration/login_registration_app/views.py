from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def registration(request):
    return render(request, "registration.html")

def success(request):
    if 'uuid' not in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['uuid'])
    }
    return render(request, "success.html", context)

#redirect functions ************************************
def add_user(request):
    errors = User.objects.user_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
            # messages.error(request, 'Email box full', extra_tags='email')
        return redirect('/')
    else:
        print(request.POST)
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        print(pw_hash)
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            birthdate = request.POST['birthdate'],
            password = pw_hash,
        )
    request.session['uuid'] = user.id
    return redirect('/success')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')
    else:
        print(request.POST)
        user = User.objects.get(email=request.POST['email'])
        print(user.password)
        if user:
            logged_user = user
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['uuid'] = logged_user.id
                return redirect('/success')
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')