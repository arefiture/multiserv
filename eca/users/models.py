from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)
    
    class Meta:
        swappable = 'AUTH_USER_MODEL'
