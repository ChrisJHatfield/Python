from django.shortcuts import render, redirect

def index(request):
    if 'session_counter' in request.session:
        # request.session['name'] = request.POST['name']
        request.session['session_counter'] += 1
        print('key exists!')
    else:
        print("key 'session_counter' does NOT exist")
        request.session['session_counter'] = 0
    return render(request, 'index.html')

def reset(request):
    del request.session['session_counter']
    return redirect('/')