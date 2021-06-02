from rest_framework import serializers
from posts.models import Post
from accounts.serializers import UserSerializer


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.ReadOnlyField(source="user.username")
    user_id = serializers.ReadOnlyField(source="user.id")
    title = serializers.CharField()
    content = serializers.CharField()
    url = serializers.URLField()
    like = UserSerializer(many=True, read_only=True)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)