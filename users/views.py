from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User

class UserRegisterView(View):
    def get(self, request):
        return render(request, "log/register.html")

    def post(self, request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        usersname = request.POST["username"]
        password = request.POST["password"]
        password_2 = request.POST["password_2"]

        user = User(first_name = first_name, last_name= last_name, email= email, usersname = usersname)
        user.set_password(password)
        user.save()
        return redirect("landing")
    
class UserLoginView(View):
    def get(self, request):
        return render(request, "log/login.html")
    
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]

        user = User.objects.filter(username = username, password = password)
        if user:
            return redirect("landing")
        else:
            return render(request, "not_found.html")
