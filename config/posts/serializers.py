from rest_framework import serializers
from posts.models import Post

from django.conf import settings
from accounts.serializers import UserSerializer

import uuid
import base64
import urllib.request
from decouple import config

MAPS_API_KEY = config("MAPS_API_KEY")


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.ReadOnlyField(source="user.username")
    profile = serializers.ImageField(source="user.profile", read_only=True)
    user_id = serializers.ReadOnlyField(source="user.id")
    title = serializers.CharField()
    content = serializers.CharField()
    url = serializers.URLField()
    cover = serializers.ImageField(read_only=True)
    like = UserSerializer(many=True, read_only=True)

    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        url = validated_data["url"]
        split_url = url.split(",")
        lat = float(split_url[0].split("@")[1])
        lng = float(split_url[1])
        pitch = float(split_url[5].split("t")[0]) - float(90)
        heading = float(split_url[4].replace("h", ""))

        base_url = "https://maps.googleapis.com/maps/api/streetview?size=400x400"

        request_url = f"{base_url}&location={lat},{lng}&fov=80&pitch={pitch}&heading={heading}&key={MAPS_API_KEY}"
        image_name = f"{uuid.uuid4()}.jpg"
        save_path = f"{settings.MEDIA_ROOT}/cover/{image_name}"
        urllib.request.urlretrieve(request_url, save_path)

        cover = f"cover/{image_name}"
        return Post.objects.create(**validated_data, cover=cover)
