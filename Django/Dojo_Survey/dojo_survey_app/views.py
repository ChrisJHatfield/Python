from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return render(request, 'index.html')

def create_survey(request):
    print(request.POST)
    return redirect('/result')

def result(request):
    print(request.POST)
    name = (request.POST['name'])
    location = (request.POST['location'])
    language = (request.POST['language'])
    comment = (request.POST['comment'])
    context = {
        'name' : name,
        'location' : location,
        'language' : language,
        'comment' : comment
    }
    return render(request, 'result.html', context)