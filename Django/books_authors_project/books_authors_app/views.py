from django.shortcuts import render, redirect
from .models import Book, Author

# render templates **************************************************
def index(request):
    context = {
        'books_table' : Book.objects.all(),
    }
    return render(request, "index.html", context)

def book_page(request, book_id):
    book_id = Book.objects.get(id=4)
    context = {
        'book_4' : book_id,
        'all_authors' : Author.objects.all(),
    }
    return render(request, "books.html", context)

def authors(request):
    context = {
        'authors_table' : Author.objects.all(),
    }
    return render(request, 'authors.html', context)

def author_page(request, author_id):
    author_id = Author.objects.get(id=5)
    context = {
        'author_5' : author_id,
        'all_books' : Book.objects.all(),
    }
    return render(request, 'author.html', context)

# redirect Book functions **********************************************
def add_book(request):
    print(request.POST)
    Book.objects.create(
        title = request.POST['title'],
        description = request.POST['description'],
    )
    return redirect('/')

def add_author_to_book(request):
    print(request.POST)
    author_name = request.POST['add_author']
    book_id = Book.objects.get(id=4)
    print(book_id, author_name)
    book_id.authors.add(author_name)
    return redirect('/books/1')

# redirect Author functions ********************************************
def add_author(request):
    print(request.POST)
    Author.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        notes = request.POST['notes'],
    )
    return redirect('/authors')

def add_book_to_author(request):
    print(request.POST)
    book_id = request.POST['add_book']
    book_to_add = Book.objects.get(id=book_id)
    author_id = Author.objects.get(id=5 )
    print(author_id, book_to_add)
    book_to_add.authors.add(author_id)
    return redirect('/authors/5')