from django.urls import path
from . import views

#wall_app urls********************************
urlpatterns = [
    #render paths*****************************
    path('', views.wallboard),
    path('/wall', views.wallboard),
    #redirect paths***************************
    path('logout', views.logout),
]