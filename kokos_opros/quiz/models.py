from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=40)


class Question(models.Model):
    question = models.CharField(max_length=120)
    answer = models.CharField(max_length=120)
    quiz = models.ForeignKey(Quiz,
                             related_name='questions',
                             on_delete=models.CASCADE)
