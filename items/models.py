from django.db import models

class Item(models.Model):
    item_header = models.ForeignKey()
    bullets = models.ForeignKey()

class ItemHeader(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300)
    date_started = models.CharField(max_length=50)
    date_ended = models.CharField(max_length=50)
    current = models.BooleanField()
    icon = models.ImageField()
    content = models.TextField()

class ItemBulletPoint(models.Model):
    