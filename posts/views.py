from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Post
from .forms import PostForm, CommentForm


# Create your views here.
def posts(request):
    return render(request, 'posts/posts.html', {
        "posts": Post.objects.all()
    })


def post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        form = CommentForm
        current_user = request.user.profile
    except Post.DoesNotExist:
        raise Http404("Post not found.")

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = current_user
            comment.save()
            return redirect('posts:post', post_id=post_id)
    
    return render(request, "posts/post.html", {
        "post": post,
        "form": form
    })


@login_required(login_url='login')
def update_post(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:posts')
    
    return render(request, 'posts/post_form.html', {
        'form': form,
        'edit': True
    })


@login_required(login_url='login')
def create_post(request):
    form = PostForm()
    current_user = request.user.profile

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            
            post = form.save(commit=False)
            post.author = current_user
            post.save()
            
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
