from django.urls import path
from .views import BooksListView, BookDetailList,home_page

urlpatterns = [
    path("library/", BooksListView.as_view(), name='library'),
    path("<int:id>/", BookDetailList.as_view(), name='book-detail'),
    path("", home_page, name='home'),
]
