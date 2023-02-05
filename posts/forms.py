from django.forms import ModelForm
from .models import Post, Comment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'futured_image',
                  'body']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
