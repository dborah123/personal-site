from django.db import models 

class Post(models.Model):
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=100)
    date_posted = models.DateField()

class PostHeader(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    header = models.CharField(max_length=200)
    subheader = models.CharField(max_length=300)

class PostItem(models.Model):
    type = models.IntegerField()
    image = models.ImageField()
    content = models.TextField()

