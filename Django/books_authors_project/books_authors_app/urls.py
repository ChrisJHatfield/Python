from django.urls import path
from . import views

urlpatterns = [
    # render paths
    path('', views.index),
    path('books/<int:book_id>', views.book_page),
    path('authors', views.authors),
    path('authors/<int:author_id>', views.author_page),
    # redirect book paths
    path('books/add', views.add_book),
    path('books/add_author', views.add_author_to_book),
    # redirect author paths
    path('authors/add', views.add_author),
    path('authors/add_book', views.add_book_to_author),
    
]