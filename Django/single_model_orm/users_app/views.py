from django.shortcuts import render
from .models import User

def index(request):
    User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email_address = request.POST['email_address'],
        age = int(request.POST['age']),
    )
    return render(request, "index.html")
