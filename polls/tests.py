import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_recent_question(self):
        q = Question(pub_date=timezone.now() - datetime.timedelta(hours=1))
        self.assertIs(q.was_published_recently(), True)


class IndexViewTests(TestCase):
    def test_index_page_loads(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
