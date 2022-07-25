from django.contrib.auth.models import AbstractUser
from django.forms import IntegerField


class User(AbstractUser):
    golden_coins = IntegerField()
