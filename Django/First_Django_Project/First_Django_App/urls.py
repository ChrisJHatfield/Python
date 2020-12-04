from django.urls import path
from . import views
urlpatterns = [
    path('', views.root_method),
    path('blogs', views.index),
    path('blogs/new', views.new),
    path('blogs/create', views.create),
    path('blogs/<int:number>', views.show),
    path('blogs/<int:number>/edit', views.edit),
    path('blogs/<int:number>/delete', views.destroy),
    # path('redirected_route', views.root_method),
    # path('/blogs/json', views.json_response),
]















# from django.urls import path
# from . import views
# urlpatterns = [
#     path('', views.root_method),
#     path('/another_route', views.another_method),
#     path('/redirected_route', views.redirected_method
# ]