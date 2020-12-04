from django.urls import path
from . import views

#login_register_app urls***********************
urlpatterns = [
    #render paths******************************
    path('', views.home),
    #redirect paths****************************
]