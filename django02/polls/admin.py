from django.contrib import admin
from .models import Question, Choice


# TabularInline 以表格形式展示
class ChoiceInline(admin.TabularInline):
    model = Choice
    # 默认提供3个选项字段
    extra = 3


# 设置Question模型显示哪些字段
class QuestionAdmin(admin.ModelAdmin):
    # 字段放在一起展示
    # fields = ['pub_date', 'question_text']
    # 字段分组展示
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    # 添加投票内容
    inlines = [ChoiceInline]
    # 显示的字段
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 添加“过滤器”侧边栏，允许以pub_date字段来过滤列表
    list_filter = ['pub_date']
    # 查询字段
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)

