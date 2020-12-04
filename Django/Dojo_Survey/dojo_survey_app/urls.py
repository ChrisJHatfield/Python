from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_survey', views.create_survey),
    path('result', views.result),
]
