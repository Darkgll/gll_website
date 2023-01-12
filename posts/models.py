from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator ,MaxLengthValidator


class Post(models.Model):
    title = models.CharField(max_length=100, validators=[MaxLengthValidator(100)])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subtitle = models.CharField(max_length=100, validators=[MaxLengthValidator(100)])
    futured_image = models.ImageField(null=True, blank=True, default="eyes-block-2.png")
    body = models.TextField(max_length=1000, validators=[MaxLengthValidator(1000)])

    def __str__(self) -> str:
        return f'Title: "{self.title}", subtitle: "{self.subtitle}", author username: "{self.author.username}"'


# class Comment(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     body = models.TextField(max_length=1000, validators=[MaxLengthValidator(1000)])

#     def __str__(self) -> str:
#         return f'Author: "{self.author}", body: "{self.body}"'
