from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Book  # make sure you have a Book model defined


@login_required(raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
