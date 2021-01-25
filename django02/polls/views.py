from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question


# 测试
def index(request):
    # 表示获取Question中 按照put_date倒叙 5条数据
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


# 问题描述：可以接收参数的视图 %s 接收数字
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


# 问题描述：detail 另一个写法
def results(request, question_id):
    reponse = 'you are looking at question %s results.'
    return HttpResponse(reponse % question_id)


# 问题得票数
def vote(request, question_id):
    return HttpResponse('you are voting on question %s.' % question_id)
