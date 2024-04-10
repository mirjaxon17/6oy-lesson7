from django.shortcuts import render
from django.views import View
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin


class BooksListView(LoginRequiredMixin, View):
    def get(self, request):
        search = request.GET.get("search")
        if not search:
            books = Book.objects.all()
            context = {
                "books" : books,
                "search":search,
            }
            return render(request, "library.html", context)
        else:
            books = Book.objects.filter(title__icontains= search) | Book.objects.filter(id__icontains= search)
            if books:
                context = {
                    "books" : books,
                    "search":search,
                }
                return render(request, "library.html", context)
            else:
                return render(request, "not_found.html")



class BookDetailList(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        return render(request, "book_detail.html", context={"book":book})

def home_page(request):
    return render(request, "home.html")