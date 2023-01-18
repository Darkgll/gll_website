from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    short_info = models.CharField(max_length=200, null=True, blank=True)
    interests_info = models.CharField(max_length=300, null=True, blank=True)
    dream_info = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/empty-profile-1.png')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}'
