from django.shortcuts import render
from django.views import View
from .models import Student


class StudentListView(View):
    def first_name(self, request):
        students = Student.objects.all()
        context = {
            "students": students
        }
        return render(request, "students.html", context)
# def student_page(request):
#     return render(request, 'students.html')
# def students_page(request):
#     return render(request, "students.html")

class LandingView(View):
    def get(self, request):
        return render(request, "landing.html")