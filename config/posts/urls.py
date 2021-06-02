from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostListCreate.as_view()),
]