from django.shortcuts import render, redirect
from .models import Dojo, Ninjas

def index(request):
    context = {
        "all_the_dojos" : Dojo.objects.all(),
    }
    return render(request, 'index.html', context)

def add_dojo(request):
    Dojo.objects.create(
        name = request.POST['name'],
        city = request.POST['city'],
        state = request.POST['state'],
        description = request.POST['description'],
    )
    return redirect('/')

def add_ninja(request):
    print(request.POST)
    location = request.POST['dojo']
    dojo_id = Dojo.objects.get(name = location)
    Ninjas.objects.create(
        dojo = dojo_id,
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
    )
    return redirect('/')

def delete_dojo(request, dojo_id):
    print("deleted: dojo_id")
    to_delete = Dojo.objects.get(id=dojo_id)
    to_delete.delete()
    return redirect('/')