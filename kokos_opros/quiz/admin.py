from django.contrib import admin
from .models import Answer, Quiz, Question

admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(Answer)
