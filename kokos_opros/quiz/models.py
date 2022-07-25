from django.db import models


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
    answer = models.CharField(max_length=120)
    wrong_answer_1 = models.CharField(max_length=120)
    wrong_answer_2 = models.CharField(max_length=120)
    wrong_answer_3 = models.CharField(max_length=120)
    
    def __str__(self):
        return self.question
