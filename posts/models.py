from django.db import models
from django.forms import IntegerField 

class Post(models.Model):
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=100)
    date_posted = models.DateField()

    def __str__(self) -> str:
        return f"Post: id: {self.id}\tauthor: {self.author}\tdate: {self.date_posted}"

class PostHeader(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    header = models.CharField(max_length=200)
    subheader = models.CharField(max_length=300)

    def __str__(self) -> str:
        return f"PostHeader: id:{self.id}\t{self.header}\t:\t{self.subheader}"

class PostItem(models.Model):
    order = IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    type = models.IntegerField()
    image = models.ImageField(blank=True)
    content = models.TextField()

    def __str__(self) -> str:
        if (self.type): content_type = "image"
        else: content_type = "paragraph"
        return f"PostItem: id{self.id}\t{content_type}"
