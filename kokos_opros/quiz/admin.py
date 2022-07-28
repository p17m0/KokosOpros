from django.contrib import admin
from .models import Answer, AnswerAmount, Quiz, Question


admin.site.register(Quiz)
admin.site.register(Answer)


class AnswersInline(admin.TabularInline):
    model = AnswerAmount
    min_num = 4
    max_num = 4


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = (AnswersInline,)
