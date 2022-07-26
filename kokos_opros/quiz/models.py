from ast import Num
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxLengthValidator

User = get_user_model()


class Quiz(models.Model):
    DIFFICULT = [
        ('HARD', 'Hard'),
        ('NORMAL', 'Normal'),
        ('SIMPLE', 'Simple'),
    ]
    name = models.CharField(max_length=40)
    questions = models.ManyToManyField('Question',
                                       related_name='questions')
    min_right = models.IntegerField()
    difficult = models.CharField(max_length=10, choices=DIFFICULT)

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.CharField(max_length=120)
    answers = models.ManyToManyField('Answer',
                                     related_name='answers',)
    num_of_right_answer = models.IntegerField()

    def __str__(self):
        return self.question


class Answer(models.Model):
    answer = models.CharField(max_length=120)

    def __str__(self):
        return self.answer

