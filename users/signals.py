from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import Profile

def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        username = user.username
        email = user.email

        Profile.objects.create(
            username=username,
            email=email,
            user=user)


def update_user(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        try:
            user.first_name = profile.name.split(' ')[0]
            user.last_name = profile.name.split(' ')[1]
        except:
            user.first_name = profile.name
            user.last_name = ''
        user.save()


def delete_user(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass


post_save.connect(receiver=create_profile, sender=User)
post_save.connect(receiver=update_user, sender=Profile)
post_delete.connect(receiver=delete_user, sender=Profile)
