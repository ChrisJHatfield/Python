from django.urls import path
from . import views

urlpatterns = [
    #render page paths****************************************
    path('', views.home),
    path('books', views.books),
    #redirect paths for user**********************************
    path('register/user', views.register),
    path('login/user', views.login),
    path('logout/user', views.logout),
    #redirect paths for books*********************************
    path('books/add', views.add_favorite_book),
]