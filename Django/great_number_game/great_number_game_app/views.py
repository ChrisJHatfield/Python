from django.shortcuts import render, redirect
import random

def index(request):
    if 'number_to_guess' not in request.session:
        my_number = random.randint(1, 100)
        request.session['number_to_guess'] = my_number
    if 'session_counter' in request.session:
        request.session['session_counter'] += 1
    else:
        request.session['session_counter'] = 0
    return render(request, "index.html")

def submitted(request):
    request.session['your_guess'] = int(request.POST['your_guess'])
    if request.session['your_guess'] > request.session['number_to_guess']:
        request.session['user_result'] = "Too high!"
    if request.session['your_guess'] < request.session['number_to_guess']:
        request.session['user_result'] = "Too low!"
    if request.session['your_guess'] == request.session['number_to_guess']:
        request.session['user_result'] = "Same!"
    elif request.session['session_counter'] > 3:
        request.session['user_result'] = "You lose!"
    return redirect('/')

def reset(request):
    request.session.flush() 
    return redirect('/')