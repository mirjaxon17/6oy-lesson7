from django.contrib import admin
from .models import Book, Author, BookingBook, Comments
from import_export.admin import ImportExportModelAdmin


@admin.register(Comments)
class CommentsAdmin(ImportExportModelAdmin):
    list_display = ("id","text" )
    list_display_links = ("id","text" )
    search_fields = ("text",)
    ordering = ("id",)

@admin.register(BookingBook)
class BookingBookAdmin(ImportExportModelAdmin):
    list_display = ("id", "take_date", "returned_date")
    list_display_links = ("id", "take_date", "returned_date")
    search_fields = ("student", "book")
    ordering = ("id",)


@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ("id","first_name", "last_name", "birth_date")
    list_display_links = ("id","first_name", "last_name", "birth_date")
    search_fields = ("id", "first_name")



@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ("id","title", "description_obj", "price", "count", "author", "create_date")
    list_display_links = ("id",  "title", "description_obj", "price", "count", "author", "create_date")
    search_fields = ("id", "title")
    ordering = ("id",)
    autocomplete_fields = ("author",)

    def description_obj(self, obj):
        return obj.descriptions[:5]






