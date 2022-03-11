from multiprocessing import managers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from posts.serializer import PostSerializer, PostHeaderSerializer
from .models import Post, PostHeader

""" GET ROUTES """
# Posts #########################################################
@api_view(["GET"])
def get_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_post(request, pk):
    post = Post.objects.get(pk=pk)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)

# PostHeaders ###################################################
@api_view(["GET"])
def get_post_headers(request):
    post_headers = PostHeader.objects.all()
    serializer = PostHeaderSerializer(post_headers, many=True)
    return Response(serializer.data)

@api_view(["Get"])
def get_post_header(request, pk):
    post_header = PostHeader.objects.get(pk=pk)
    serializer = PostHeaderSerializer(post_header, many=False)
    return Response(serializer.data)

@api_view(["GET"])
def get_post_header_by_title(request, title):
    post_header = PostHeader.objects.get(header=title)
    serializer = PostSerializer(post_header, many=False)
    return Response(serializer.data)

@api_view(["GET"])
def get_post_header_by_post(request, pk):
    post_header = PostHeader.objects.get(post=pk)
    serializer = PostSerializer(post_header, many=False)
    return Response(serializer.data)

""" DOCUMENTATION ROUTES """
@api_view(["GET"])
def get_routes(request):
    routes = [
        {
            "Endpoint": "/posts/",
            "method": "GET",
            "body": None,
            "decription": "Returns an array of posts"
        },
        {
            "Endpoint": "/posts/<int:pk>",
            "method": "GET",
            "body": None,
            "description": "Returns a post with given id",
        },
        {
            "Endpoint": "/headers/",
            "method": "GET",
            "body": None,
            "description": "Returns an array of postheaders",
        },
        {
            "Endpoint": "/headers/<int:pk>",
            "method": "GET",
            "body": None,
            "description": "Returns a postheader with given id",
        },
        {
            "Endpoint": "/headers/title=<int:pk>",
            "method": "GET",
            "body": None,
            "description": "Returns a postheader with title 'title'",
        },
        {
            "Endpoint": "/header.post_id=<int:pid>",
            "method": "GET",
            "body": None,
            "description": "Returns a postheader with a post with given id",
        },
    ]
    return Response(routes)