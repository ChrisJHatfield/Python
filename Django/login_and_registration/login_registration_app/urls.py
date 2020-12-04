from django.urls import path
from . import views

urlpatterns = [
    #Render routes*************************
    path('', views.registration),
    path('success', views.success),
    #Redirect routes***********************
    path('user/new', views.add_user),
    path('user/login', views.login),
    path('logout', views.logout),
    
]