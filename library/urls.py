from django.urls import path
from .views import BooksListView, home_page

urlpatterns = [
    path("library/", BooksListView.as_view(), name='library'),
    path("", home_page, name='home'),
]
