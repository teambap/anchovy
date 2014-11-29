from django.db import models

class Item(models.Model):
    user_id = models.IntegerField(max_length=11)
    name = models.CharField(max_length=200)
    link = models.URLField()
    registered = models.DateField()
    updated = models.DateField()
    status = models.CharField(max_length=2)