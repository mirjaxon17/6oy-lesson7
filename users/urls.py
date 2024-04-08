from django.urls import path
from .views import UserRegisterView, UserLoginView

urlpatterns = [
    path("users/register/", UserRegisterView.as_view(), name="registor"),
    path("users/login/", UserLoginView.as_view(), name="login"),
]