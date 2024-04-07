from django.shortcuts import render
from django.views import View
from .models import Book

class BooksListView(View):
    def get(self, request):
        books = Book.objects.all()
        context = {
            "books" : books
        }
        return render(request, "library.html", context)

def home_page(request):
    return render(request, "home.html")