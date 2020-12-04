from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Shows


# Render page functions**********************************************
def shows(request):
    context = {
        'all_shows' : Shows.objects.all(),
    }
    return render(request, 'shows.html', context)

def create(request):
    return render(request, 'create.html')

def show_page(request, show_id):
    context = {
        'show_info' : Shows.objects.get(id=show_id),
    }
    return render(request, 'show_page.html', context)

def edit_page(request, show_id):
    context = {
        'show_info' : Shows.objects.get(id=show_id),
    }
    return render(request, 'edit_show.html', context)

# Redirect page functions**********************************************
def root(request):
    return redirect('/shows')

def add_show(request):
    print(request.POST)
    errors = Shows.objects.basic_validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        newly_created_show = Shows.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            release_date = request.POST['release_date'],
            description = request.POST['description'],
        )
        return redirect(f'/shows/{newly_created_show.id}')

def update_show(request, show_id):
    print(request.POST)
    print(show_id)
    errors = Shows.objects.basic_validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{show_id}/edit')
    else:
        update_show = Shows.objects.get(id=show_id)
        update_show.title = request.POST['title']
        update_show.network = request.POST['network']
        update_show.release_date = request.POST['release_date']
        update_show.description = request.POST['description']
        update_show.save()
        return redirect(f'/shows/{update_show.id}')

def destroy(request, show_id):
    destroy_show = Shows.objects.get(id=show_id)
    destroy_show.delete()
    return redirect('/shows')

# Validations Function
def update(request, id):
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect