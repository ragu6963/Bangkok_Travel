from posts.models import Post
from posts.serializers import PostSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PostListCreate(APIView):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
