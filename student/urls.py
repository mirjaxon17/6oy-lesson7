from django.urls import path
from .views import LandingView, StudentListView

urlpatterns = [
    path("students/", StudentListView.as_view(), name='students'),
    path("landing/", LandingView.as_view(), name='landing'),
]
