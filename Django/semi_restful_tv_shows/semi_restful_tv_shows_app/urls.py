from django.urls import path
from . import views

urlpatterns = [
# page render paths****************************
    path('shows', views.shows),
    path('shows/new', views.create),
    path('shows/<int:show_id>', views.show_page),
    path('shows/<int:show_id>/edit', views.edit_page),
# redirect paths*******************************
    path('', views.root),
    path('shows/create', views.add_show),
    path('shows/<int:show_id>/update', views.update_show),
    path('shows/<int:show_id>/destroy', views.destroy),
]