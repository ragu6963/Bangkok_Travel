from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path("", views.home, name="home"),
    path("index/", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:post_pk>/", views.detail, name="detail"),
    path("<int:post_pk>/update/", views.update, name="update"),
    path("<int:post_pk>/delete/", views.delete, name="delete"),
    path(
        "<int:post_pk>/comment_create",
        views.comment_create,
        name="comment_create",
    ),
    path("like/", views.like, name="like"),
]