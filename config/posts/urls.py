from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostListCreate.as_view()),
    path("<int:post_id>/", views.PostDetailUpdateDelete.as_view()),
    path("profile/<int:user_id>/", views.UserPostList.as_view()),
]
