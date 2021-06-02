from django.db import models
from django.conf import settings


class Post(models.Model):
    # user 관계 생성
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    # 대륙 카테고리
    category = models.TextField(default="아시아")

    # # 위도 경도
    # lat = models.FloatField()
    # lng = models.FloatField()

    # # static street view 설정 값
    # heading = models.FloatField(default=0.0)
    # pitch = models.FloatField(default=90.0)

    # 스트리트 뷰 주소
    url = models.URLField(default="")

    # static street view image 경로
    static_image = models.ImageField(default="static/img/default.png")

    # 좋아요 User:Post = N:M
    like = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_posts", blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
