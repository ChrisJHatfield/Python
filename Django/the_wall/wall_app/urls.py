
from django.urls import path
from . import views

urlpatterns = [
    #Render Paths****************************
    path('', views.home),
    path('wall', views.wall),
    #Redirect Paths****************************
    path('register/new-user', views.register),
    path('login/user', views.login),
    path('message/posted', views.new_message),
    path('comment/posted', views.new_comment),
    path('message/<int:message_id>/delete', views.delete_message),
    path('wall/logout', views.logout),
]