from django.shortcuts import render
from time import strftime, localtime

def index(request):
    context = {
        "time": strftime("%b %d, %Y %I:%M %p", localtime())
    }
    return render(request, "index.html", context)