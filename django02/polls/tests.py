import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question
'''
自动化测试：
python manage.py test polls 将会寻找 polls 应用里的测试代码
它找到了 django.test.TestCase 的一个子类
它创建一个特殊的数据库供测试使用
它在类中寻找测试方法——以 test 开头的方法。
在 test_was_published_recently_with_future_question 方法中，它创建了一个 pub_date 值为 30 天后的 Question 实例。
接着使用 assertls() 方法，发现 was_published_recently() 返回了 True，而我们期望它返回 False。
'''

# 创建投票问题
def create_question(question_text, days):
    time = timezone.now() + datetime.timezone(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    # 测试没有数据
    def test_no_question(self):
        reponse = self.client.get(reverse('polls:index'))
        self.assertEqual(reponse.status_code, 200)
        # 返回的网页上时候包含如下消息
        self.assertContains(reponse, 'no polls are available.')
        # latest_question_list 是否为空
        self.assertQuerysetEqual(reponse.context['latest_question_list'], [])

    # 测试过去的数据 是否在列表中
    def test_past_question(self):
        create_question(question_text='past question.', days=-30)
        reponse = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            reponse.context['latest_question_list'],
            ['Question: Past question.']
        )

    # 测试将来的数据
    def test_future_question(self):
        create_question(question_text='Future question.', days=30)
        reponse = self.client.get(reverse('polls:index'))
        self.assertContains(reponse, 'no polls are available.')
        self.assertQuerysetEqual(reponse.context['latest_question_list'], [])

    # 测试两个过去的数据
    def test_two_past_question(self):
        create_question(question_text='Past question 1.', days=-30)
        create_question(question_text='Past question 2.', days=-5)
        reponse = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            reponse.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """测试将来的数据不存在"""
        future_question = create_question(question_text='Future quesion.', days=5)
        url = reverse('polls:detail', args=(future_question.id, ))
        reponse = self.client.get(url)
        self.assertEqual(reponse.status_code, 404)

    def test_past_question(self):
        """测试存在过去的数据"""
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id, ))
        reponse = self.client.get(url)
        self.assertContains(reponse, past_question.question_text)