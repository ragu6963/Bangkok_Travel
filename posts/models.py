from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 대륙 카테고리
    category = models.TextField(default="아시아")
    # 위도 경도
    lat = models.FloatField()
    lng = models.FloatField()
    # 스트리트 뷰 주소
    url = models.URLField(default="")
    # user 관계 생성
    user = models.ForeignKey(User, on_delete=models.CASCADE)
