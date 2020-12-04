from django.shortcuts import render

# login_register_app views**************
#render functions***********************
def home(request):
    return render(request, 'home.html')