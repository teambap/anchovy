from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User)
    # email = models.EmailField(
    #     verbose_name='email address',
    #     max_length=255,
    #     unique=True,
    # )
    profile_image_url = models.CharField(max_length=250, blank=True, null=True)
    # REQUIRED_FIELDS = ['profile_image_url']
    # USERNAME_FIELD = 'email'

