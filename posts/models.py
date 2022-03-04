from django.db import models 

class Post(models.Model):
    post_header = models.OneToOneField()

class PostHeader(models.Model):

class PostItem(models.Model):
    type = models.IntegerField()
    image = 

