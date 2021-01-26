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
    path('', views.IndexView.as_view(), name='index'),
    # /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),



]