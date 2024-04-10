from django.urls import path
from .views import UserRegisterView, UserLoginView, LOgOUtView

urlpatterns = [
    path("users/register/", UserRegisterView.as_view(), name="registor"),
    path("users/login/", UserLoginView.as_view(), name="login"),
    path("users/logout/", LOgOUtView.as_view(), name="logout"),
]