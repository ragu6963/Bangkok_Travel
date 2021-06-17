from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail


class User(AbstractUser):
    followings = models.ManyToManyField("self", symmetrical=False, related_name="followers")
    nickname = models.CharField(max_length=20)
    introduction = models.TextField(null=True)
    profile = ProcessedImageField(
        upload_to="images/%Y/%m/%d/",
        processors=[Thumbnail(200, 200)],
        options={"quality": 60},
        default="default_profile.png",
    )
