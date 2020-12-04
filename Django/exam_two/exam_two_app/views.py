from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Wish
import bcrypt

def home(request):
    return render(request, 'registration.html')

def wishes(request):
    if 'uuid' not in request.session:
        return redirect('/')
    user_in_session = User.objects.get(id=request.session['uuid'])
    context = {
        'user' : user_in_session,
        'all_wishes' : user_in_session.wisher.all(),
        'all_user_wishes': Wish.objects.all(),
    }
    return render(request, 'wishes.html', context)

def new_wish(request):
    if 'uuid' not in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['uuid'])
    }
    return render(request, 'create.html', context)

def edit_wish(request, wish_id):
    if 'uuid' not in request.session:
        return redirect('/')
    context = {
        'wish_obj': Wish.objects.get(id=wish_id),
        'user': User.objects.get(id=request.session['uuid']),
    }
    print(context)
    return render(request, 'edit.html', context)

def wish_stats(request):
    if 'uuid' not in request.session:
        return redirect('/')
    user_in_session = User.objects.get(id=request.session['uuid'])
    context = {
        'user' : user_in_session,
        'all_granted_wishes' : Wish.objects.filter(granted_wish="1"),
        'user_granted_wishes': user_in_session.wisher.filter(granted_wish='1'),
        'user_pending_wishes': user_in_session.wisher.filter(granted_wish='0'),
    }
    return render(request, 'stats.html', context)

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
    return redirect('/wishes')

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
                return redirect('/wishes')
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

#Wish Functions************************************
def edited_wish(request, wish_id):
    errors = Wish.objects.wish_validator(request.POST)
    if 'cancel' in request.POST:
        return redirect('/wishes')
    elif len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
            return redirect(f'/wishes/edit/{wish_id}')
    else:
        print(request.POST)
        update_wish = Wish.objects.get(id=wish_id)
        print(update_wish)
        update_wish.item = request.POST['wish_item']
        update_wish.description = request.POST['wish_description']
        update_wish.save()
        return redirect('/wishes')

def add_wish(request):
    errors = Wish.objects.wish_validator(request.POST)
    if 'cancel' in request.POST:
        return redirect('/wishes')
    elif len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/wishes/new')
    else:
        Wish.objects.create(
            item = request.POST['wish_item'],
            description = request.POST['wish_description'],
            wish = User.objects.get(id=request.session['uuid']),
        )
    return redirect('/wishes')

def remove_wish(request, wish_id):
    remove_wish = Wish.objects.get(id=wish_id)
    remove_wish.delete()
    return redirect('/wishes')

def granted_wish(request, wish_id):
    granted_wish_update = Wish.objects.get(id=wish_id)
    granted_wish_update.granted_wish = 1
    granted_wish_update.save()
    return redirect('/wishes')

#Liked Wish Functions************************************

def wish_liked(request, wish_id):
    user_liking = User.objects.get(id=request.session['uuid'])
    wish_liked = Wish.objects.get(id=wish_id)
    user_liking.wishes_liked.add(wish_liked)
    return redirect('/wishes')