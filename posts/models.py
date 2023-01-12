from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator ,MaxLengthValidator

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, validators=[MaxLengthValidator(100)])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subtitle = models.CharField(max_length=100, validators=[MaxLengthValidator(100)])
    img_url = models.URLField()
    body = models.TextField(max_length=1000, validators=[MaxLengthValidator(1000)])

    def __str__(self) -> str:
        return f'Title: "{self.title}", subtitle: "{self.subtitle}", author username: "{self.author.username}"'
