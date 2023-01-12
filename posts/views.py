from django.shortcuts import render
from django.http import Http404
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'posts/index.html', {
        "posts": Post.objects.all()
    })

def post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404("Post not found.")
    
    return render(request, "posts/post.html"), {
        "post": post,
        # TODO comments
        # TODO likes and dislikes (with user name)
    }
