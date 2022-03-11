from rest_framework.serializers import ModelSerializer
from .models import Post, PostHeader

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostHeaderSerializer(ModelSerializer):
    class Meta:
        model = PostHeader
        fields = '__all__'