from django.urls import path
from . import views

urlpatterns = [
#Page Render Paths**********************
    path('', views.home),
    path('wishes', views.wishes),
    path('wishes/new', views.new_wish),
    path('wishes/edit/<int:wish_id>', views.edit_wish),
#User Paths*****************************
    path('register/new-user', views.register),
    path('login/user', views.login),
    path('logout/user', views.logout),
#Wishes Paths***************************
    path('wishes/add', views.add_wish),
    path('wishes/edit/update/<int:wish_id>', views.edited_wish),
    path('wishes/remove/<int:wish_id>', views.remove_wish),
    path('wishes/granted/<int:wish_id>', views.granted_wish),
    path('wishes/stats', views.wish_stats),
#Liked Wishes Paths*********************
    path('wishes/liked/<int:wish_id>', views.wish_liked),
]