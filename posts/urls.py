from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path("", views.home, name="home"),
    path("index/", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/delete/", views.delete, name="delete"),

]