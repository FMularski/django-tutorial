from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question
from django.urls import reverse


class QuestionModelTests(TestCase):
    # each method starts with 'test'

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


def create_question(text, days):
    """
    Helper function for creating questions
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(text=text, pub_date=time)


"""
assertIs() -- comparision
assertEqual() -- comparision
assertContaints() -- containing a string
assertQuerysetEqual() -- queryset comparision
"""


class QuestionIndexViewTests(TestCase):
    """
    testing case when no questions are stored
    expecting: 'No questions found.' message
    expecting: [] as the context object of the response 
    """
    def test_no_question(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No questions found.')
        self.assertQuerysetEqual(response.context['questions'], [])

    """
    testing case when one past question is stored
    expecting: queryset with 1 question as context object of the response
    """
    def test_past_question(self):
        create_question(text='Past question.', days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['questions'],
            ['<Question: Past question.>']
        )

    """
    testing case when one future question is stored, 
    it is filtered out in the index view so it cant be displayed yet 
    expecting: 'No questions found.' message
    expecting: [] as the context object of the response
    """
    def test_future_question(self):
        create_question(text='Future question.', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, 'No questions found.')
        self.assertQuerysetEqual(response.context['questions'], [])

    """
    testing case when 1 past and 1 future question are stored
    expecting: only past question in the context object of the response
    """
    def test_future_question_and_past_question(self):
        create_question(text='Future question.', days=30)
        create_question(text='Past question.', days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['questions'], ['<Question: Past question.>'])

    """
    testing case when 2 past questions are stored
    expecting: 2 questions in the context object of the response
    """
    def test_two_past_questions(self):
        create_question(text='Past question 1.', days=-30)
        create_question(text='Past question 2.', days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['questions'],
        ['<Question: Past question 1.>', '<Question: Past question 2.>'])


class QuestionsDetailViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question(text='Future question.', days=2)
        url = reverse('polls:detail', args=(future_question.id, ))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question(text='Past question.', days=-2)
        url = reverse('polls:detail', args=(past_question.id, ))
        response = self.client.get(url)
        self.assertContains(response, past_question.text)