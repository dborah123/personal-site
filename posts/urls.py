from django.urls import path
from posts.views import (
    get_post, 
    get_post_header,
    get_post_header_by_post,
    get_post_header_by_title, 
    get_post_headers,
    get_routes, 
    get_posts
)


app_name = "posts"

urlpatterns = [
    path("documentation/", get_routes, name="documentation"),

    path("posts/", get_posts, name="posts"),
    path("posts/<int:pk>", get_post, name="post"),

    path("headers/", get_post_headers, name="postheaders"),
    path("headers/<int:pk>", get_post_header, name="postheader"),
    path("header/title=<str:title>", get_post_header_by_title, name="postbytitle"),
    path("header/post_id=<int:pid>", get_post_header_by_post, name="postheaderbypost")
]