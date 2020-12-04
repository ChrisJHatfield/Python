from django.shortcuts import render, redirect


#wall_app views*************************
#render functions***********************
def wallboard(request):
    return render(request, 'wallboard.html')
#redirect functions***********************
def logout(request):
    return redirect('/')