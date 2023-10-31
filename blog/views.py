from django.shortcuts import render
from .models import Post

all_posts = Post.objects.all().order_by("-date")


def get_date(post):
    return post["date"]


def starting_page(request):
    # django auto optimizes the below query by only creating a SQL query
    # that extract 3 entries from the database.
    latest_posts = Post.objects.all().order_by("-date")[:3]  # python negative indexing no support
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, 'blog/all-posts.html', {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
