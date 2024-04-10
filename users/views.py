from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


class UserRegisterView(View):
    def get(self, request):
        form = UserRegisterForm()

        return render(request, "log/register.html", {"form": form})

    def post(self, request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        password_2 = request.POST["password_2"]
        if password == password_2:
            user = User(first_name = first_name, last_name= last_name, email= email, username = username)
            user.set_password(password)
            user.save()
            return redirect("login")
        else:
            return render(request, 'log/register.html')
class UserLoginView(View):
    def get(self, request):
        form =  UserLoginForm()

        return render(request, "log/login.html", {"form" : form})
    
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]


        data = {
            "username": username,
            "password" : password
        }

        login_form = AuthenticationForm(data=data)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect("landing")
        else:
            form = UserLoginForm()
            context = {
                "form" : form
            }
            return render(request, "log/login.html", {"form" : form}) 
        

class LOgOUtView(View):
    def get(self, request):
        logout(request)
        return redirect("landing")

        # user = User.objects.filter(username = username, password = password)
        # if user:
        #     return redirect("landing")
        # else:
        #     return render(request, "not_found.html")
