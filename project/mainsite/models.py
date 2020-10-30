from django.db import models
from django.contrib.auth.models import AbstractUser


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f"user_{instance.user.id}/{filename}"


class User(AbstractUser):
    # Attributes of User
    # Needed when creating an user
    username = models.CharField(max_length=32, unique=True, primary_key=True)
    email = models.EmailField()
    tagDiscord = models.CharField(max_length=36, blank=False)

    # Attributes to be set after login
    description = models.TextField(blank=True, max_length=250)
    avatar = models.ImageField(upload_to=user_directory_path)
    tagSteam = models.CharField(blank=True, max_length=50)
    tagPSN = models.CharField(blank=True, max_length=50)
    tagXbox = models.CharField(blank=True, max_length=50)
    tagSwitch = models.CharField(blank=True, max_length=50)

    # Setting up some variables
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'tagDiscord']
    # TODO add games and tags
