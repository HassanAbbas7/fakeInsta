from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.TextField(max_length=14)
    last_name = models.TextField(max_length=14)
    password = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True) #auto_now = True if you want to add a field like "updated_on"
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()



class InstaData(models.Model):
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email













