from rest_framework import serializers
from posts.models import Post
from accounts.serializers import UserSerializer


class PostSerializer(serializers.Serializer):
    # id = serializers.IntegerField(label="ID", read_only=True)
    title = serializers.CharField()
    content = serializers.CharField()
    url = serializers.URLField()
    like = UserSerializer(many=True, read_only=True)

    # class Meta:
    #     model = Post
    #     fields = "__all__"

    def create(self, validated_data):
        return Post.objects.create(**validated_data)