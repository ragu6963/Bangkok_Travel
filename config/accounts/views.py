from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import get_user_model
from .models import User
from django.conf import settings
from rest_framework_jwt import utils


def jwt_payload_handler(user):
    payload = utils.jwt_payload_handler(user)
    payload["is_staff"] = user.is_staff
    payload["is_superuser"] = user.is_superuser
    return payload


@api_view(["POST"])
def signup(request):
    password = request.data.get("password")
    password_confirmation = request.data.get("passwordConfirmation")

    if password != password_confirmation:
        return Response(
            {"error": "비밀번호가 일치하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST
        )

    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get("password"))
        user.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)
