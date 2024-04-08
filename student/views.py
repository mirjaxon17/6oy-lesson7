from django.shortcuts import render
from django.views import View
from .models import Student


class StudentListView(View):
    def get(self, request):
        students = Student.objects.all()
        return render(request, "students.html", context= {"talabalar":students})
class LandingView(View):
    def get(self, request):
        return render(request, "landing.html")
    
