from django.db import models
from django.core.validators import MaxLengthValidator
from users.models import Profile
import uuid


class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=100, validators=[MaxLengthValidator(100)])
    author = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    subtitle = models.CharField(max_length=100, validators=[MaxLengthValidator(100)])
    futured_image = models.ImageField(null=True, blank=True, default="eyes-block-2.png")
    body = models.TextField(max_length=1000, validators=[MaxLengthValidator(1000)])
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Title: "{self.title}", subtitle: "{self.subtitle}", author username: "{self.author.username}"'


class Comment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Author username: "{self.author.username}", body: "{self.body}"'


# class Comment(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     body = models.TextField(max_length=1000, validators=[MaxLengthValidator(1000)])

#     def __str__(self) -> str:
#         return f'Author: "{self.author}", body: "{self.body}"'
