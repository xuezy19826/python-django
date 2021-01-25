# -*- coding：utf-8 -*-#

# --------------------------------------------------------------
# NAME:          urls
# Description:   路由
# Author:        xuezy
# Date:          2021/1/21 18:46
# --------------------------------------------------------------
from django.urls import path
from . import views

# 设置命名空间 避免不同应用的url同名
app_name = 'polls'
urlpatterns = [
    # /polls/
    path('', views.index, name='index'),
    # /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),



]