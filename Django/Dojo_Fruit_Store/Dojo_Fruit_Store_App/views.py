from django.shortcuts import render, redirect
from time import strftime, localtime

def index(request):
    return render(request, 'index.html')

def checkout(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    student_id = request.POST['student_id']
    strawberry = request.POST['strawberry']
    raspberry = request.POST['raspberry']
    apple = request.POST['apple']
    context = {
        'first_name' : first_name,
        'last_name' : last_name,
        'student_id' : student_id,
        'strawberry' : strawberry,
        'raspberry' : raspberry,
        'apple' : apple,
        'order_sum' : (int(strawberry) + int(raspberry) + int(apple)),
        'time' : strftime("%B %d %Y %I:%M:%S %p", localtime()),
        
    }
    print(request.POST)
    customer_name = (first_name + ' ' + last_name)
    order_sum = int(strawberry) + int(raspberry) + int(apple)
    print(f"Charging {customer_name} for {order_sum} fruits")
    return render(request, 'checkout.html', context)

def fruit_store(request):
    return render(request, 'fruits.html')
# Create your views here.
