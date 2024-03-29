from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path("signup/", views.signup),
    path("login/", obtain_jwt_token),
    path("profile/<int:user_id>/", views.Profile.as_view()),
]
