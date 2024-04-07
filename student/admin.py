from django.contrib import admin
from .models import Student, Address

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id","first_name", "last_name", "age", "status")
    list_display_links = ("id","first_name", "last_name", "age", "status")
    search_fields = ("first_name", "last_name", "age")
    ordering = ("id",)
    
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    list_display_links = ("id","name")
    search_fields = ("id","name")
    ordering = ("name",)

