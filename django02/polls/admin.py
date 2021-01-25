from django.contrib import admin
from .models import Question, Choice

# 投票应用
admin.site.register(Question)
admin.site.register(Choice)

