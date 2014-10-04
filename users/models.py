from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)


class Kakao(User):
    kakao_id = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    profile_image = models.CharField(max_length=100)
    thumbnail_image = models.CharField(max_length=100)

