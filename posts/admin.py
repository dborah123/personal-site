from django.contrib import admin

from posts.models import Post, PostHeader, PostItem

# Register your models here.
admin.site.register(Post)
admin.site.register(PostHeader)
admin.site.register(PostItem)