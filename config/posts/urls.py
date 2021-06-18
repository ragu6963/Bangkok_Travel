from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostListCreate.as_view()),
    path("<int:post_id>/", views.PostDetailUpdateDelete.as_view()),
    path("user/<int:user_id>/", views.UserPostList.as_view()),
    path("like/<int:post_id>/", views.PostLike.as_view()),
]
