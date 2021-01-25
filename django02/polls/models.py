import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    """问题"""
    # 问题描述
    question_text = models.CharField(max_length=300)
    # 发布时间
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    # 自定义方法：计算时间差
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    """选项"""
    # 问题
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 选项描述
    choice_text = models.FileField(max_length=200)
    # 得票数
    votes = models.IntegerField(default=0)

    # def __str__(self):
    #     return self.choice_text
