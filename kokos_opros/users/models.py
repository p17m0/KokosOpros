from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    golden_coins = models.IntegerField(default=0)
    color = models.CharField(max_length=16, default='white')
