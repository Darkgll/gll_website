from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm


# Create your views here.
def index(request):
    return render(request, 'posts/posts.html', {
        "posts": Post.objects.all()
    })


def post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404("Post not found.")
    
    return render(request, "posts/post.html", {
        "post": post,
        # TODO comments
    })


def update_post(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:posts')
    
    return render(request, 'posts/post_form.html', {
        'form': form
    })


def create_post(request):
    form = PostForm()
    current_user = request.user

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            
            project = form.save(commit=False)
            project.author = current_user
            project.save()
            
            return redirect('posts:posts')
    return render(request, 'posts/post_form.html', {
        'form': form
    })


def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('posts:posts')
    return render(request, 'posts/posts.html')
