from django.urls import path
from . import views

"""
===============
Available views
===============

> index: blog home page
> all-posts: all posts page
> post: single blog post
"""
app_name = "blog"
urlpatterns = [
    path("", views.starting_page, name="index"),
    path("all-posts", views.posts, name="all-posts"),
    path("posts/<slug:slug>", views.post_detail, name="post"),
]
