from django.db import models

class Item(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=200)
    link = models.URLField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    status = models.CharField(max_length=2)
