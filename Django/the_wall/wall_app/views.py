from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Message, Comment
import bcrypt

#Render Functions***********************************
def home(request):
    return render(request, "home.html")

def wall(request):
    if 'uuid' not in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['uuid']),
        'all_messages': Message.objects.all()
    }
    return render(request, "wall.html", context)

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
    return redirect('/wall')

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
                return redirect('/wall')
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

#Message Functions************************************
def new_message(request):
    print(request.POST)
    errors = Message.objects.message_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
    else: 
        user_posted_message = User.objects.get(id=request.session['uuid'])
        Message.objects.create(
            post = request.POST['posted_message'],
            user_message = user_posted_message,
        )
    return redirect('/wall')

def delete_message(request, message_id):
    Message.objects.get(id=message_id).delete()
    return redirect('/wall')
#Comment Functions************************************
def new_comment(request):
    print(request.POST)
    errors = Comment.objects.comment_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
    else:
        user_comment = User.objects.get(id=request.session['uuid'])
        whole_messager = Message.objects.get(id=request.POST['message_id'])
        Comment.objects.create(
            text = request.POST['posted_comment'],
            commenter = user_comment,
            message_on_comment = whole_messager,
        )
    return redirect('/wall')