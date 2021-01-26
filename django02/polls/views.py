from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice


# 主页  通用视图：ListView  显示一个对象列表信息
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


# 问题详情 通用视图：DetailView  显示一个对象信息
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    # 默认查询 发布时间 <= 当前时间 的数据
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


# 投票结果
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# 问题得票数
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST 是一个类字典对象，让你可以通过关键字的名字获取提交的数据。
        # 这个例子中， request.POST['choice'] 以字符串形式返回选择的 Choice 的 ID。 request.POST 的值永远是字符串
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # 如果在 request.POST['choice'] 数据中没有提供 choice ， POST 将引发一个 KeyError 。上面的代码检查 KeyError ，
    # 如果没有给出 choice 将重新显示 Question 表单和一个错误信息。
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'you did not select a choice.',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
