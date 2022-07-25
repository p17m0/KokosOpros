from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.db.models import IntegerField


class User(AbstractUser):
    golden_coins = IntegerField(default=0)
    done_tests = IntegerField(default=0)
