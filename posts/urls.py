from django.urls import path
from posts.views import post_view

app_name = "posts"

urlpatterns = [
    path("<slug:slug>/", post_view)
]