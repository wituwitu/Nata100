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
    nacimiento = models.DateField(null=True)
    region = models.CharField(max_length=32, default="")
    comuna = models.CharField(max_length=32, default="")
    amigues = models.ManyToManyField("self", blank=True)    # many (user) to many (user)
    # Setting up some variables
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']


class Profe(User):
    pass


class Alumne(User):
    profesor = models.ForeignKey(Profe, on_delete=models.CASCADE, null=True)  # one (profe) to many (alumne)




