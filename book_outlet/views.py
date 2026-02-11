from django.shortcuts import render
from .models import Book
from django.shortcuts import get_object_or_404

def index(request):
    books = Book.objects.all()
    return render(request, "book_outlet/index.html", {
        "books": books
    })


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "book_outlet/book_detail.html", {
        "book": book
    })