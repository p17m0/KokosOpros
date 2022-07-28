from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator


User = get_user_model()


class Quiz(models.Model):
    """
    Модель Теста.
    """
    DIFFICULT = [
        (20, 'Сложный'),
        (15, 'Нормальный'),
        (10, 'Простой'),
    ]
    name = models.CharField(verbose_name='Название теста',
                            max_length=40)
    questions = models.ManyToManyField('Question',
                                       related_name='questions')
    min_right_answers = models.IntegerField(
        verbose_name='Минимальное количество ответов для прохождение теста',
    )
    difficult = models.IntegerField(verbose_name='Сложность',
                                    default=0,
                                    choices=DIFFICULT)

    def __str__(self):
        return self.name


class Question(models.Model):
    """
    Модель вопроса.
    """
    question = models.CharField(verbose_name='Вопрос',
                                max_length=120)
    answers = models.ManyToManyField('Answer',
                                     related_name='answers',
                                     through='AnswerAmount')
    num_of_right_answer = models.IntegerField(
        verbose_name='Номер правильного ответа',
        validators=(MinValueValidator(1),
                    MaxValueValidator(4)))

    def __str__(self):
        return self.question


class Answer(models.Model):
    """
    Модель вопроса.
    """
    answer = models.CharField('Ответ',
                              max_length=120)

    def __str__(self):
        return self.answer


class AnswerAmount(models.Model):
    """
    Количество ответов.
    """
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='amounts',
        verbose_name='Вопрос'
    )
    answer = models.ForeignKey(
        Answer,
        on_delete=models.CASCADE,
        related_name='amounts',
        verbose_name='Ответ'
    )


class DoneQuiz(models.Model):
    """
    Модель пройденный тестов пользоателем.
    """
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='userdonequizs')
    quiz = models.ForeignKey(Quiz,
                             on_delete=models.CASCADE,
                             related_name='donequizs')
    done = models.BooleanField()
