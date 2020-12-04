from django.shortcuts import render, redirect
import random
from time import strftime, localtime

def index(request):
    return render(request, 'index.html')

def process_money(request):
    context = {
        'time' : strftime("%Y/%m/%d  %I:%M %p", localtime()),
    }
    if "total_gold" not in request.session:
        request.session["total_gold"] = 0
    if "activities" not in request.session:
        request.session['activities'] = []

    if request.POST['building'] == 'farm':
        farm = random.randint(10, 20)
        print(farm)
        request.session["total_gold"] += farm
        print(request.session['total_gold'])
        request.session['activities'].append(f"Earned {farm} gold from the farm! ({context['time']})")
        request.session.modified = True
        return redirect('/')
    if request.POST['building'] == 'cave':
        cave = random.randint(5, 10)
        print(cave)
        request.session["total_gold"] += cave
        print(request.session['total_gold'])
        request.session['activities'].append(f"Found {cave} gold in the cave! ({context['time']})")
        request.session.modified = True
        return redirect('/')
    if request.POST['building'] == 'house':
        house = random.randint(2, 5)
        print(house)
        request.session["total_gold"] += house
        print(request.session['total_gold'])
        request.session['activities'].append(f"You found {house} gold while cleaning the house! ({context['time']})")
        request.session.modified = True
        return redirect('/')
    if request.POST['building'] == 'casino':
        casino = random.randint(-50, 50)
        print(casino)
        request.session["total_gold"] += casino
        print(request.session['total_gold'])
        if casino > 0:
            request.session['activities'].append(f"You won {casino} gold at the slots! ({context['time']})")
            request.session.modified = True
            return redirect('/')
        elif casino < 0:
            request.session['activities'].append(f"Tough loss of {casino} gold. Looks like the house wins this time! ({context['time']})")
            request.session.modified = True
            return redirect('/')







    
    # context = {
    #     'farm' : farm,
    #     'time' : strftime("%B %d %Y %I:%M:%S %p", localtime()),
    # }
    # if request.POST == ['farm']:
    #     farm = random.randint(10, 20) 
    #     print(f"Farm gives you: {'farm'} gold!")
    #     return redirect('/', context)
    # else:
    #     return redirect('/')



# farm = random.randint(10, 20)
#     cave = random.randint(5, 10)
#     house = random.randint(2, 5)
# = random.randint(10, 20) 