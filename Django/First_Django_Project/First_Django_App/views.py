from django.shortcuts import render, HttpResponse, redirect

def root_method(request):
    return HttpResponse ("render_page")
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def create(request):
    return redirect("/")
def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")
def edit(request, number):
    print(type(number))
    return HttpResponse(f"placeholder to edit blog {number}")
def destroy(request, number):
    return HttpResponse(f"to be deleted {number}")










# def json_response(request):
#     return JsonResponse({"response": "title: My first blog, content: Lorem ipsum dolor sit amet consectetur adipisicing elit.", "status": True})

# Create your views here.






# from django.shortcuts import HttpResponse, redirect # add redirect to import statement
# from django.http import JsonResponse
# def root_method(request):
#     return HttpResponse("String response from root_method")
# def another_method(request):
#     return redirect("/redirected_route")
# def redirected_method(request):
#     return JsonResponse({"response": "JSON response from redirected_method", "status": True})
