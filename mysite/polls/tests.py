from django.test import TestCase
from .models import Question, Choice
import datetime 
from django.utils import timezone

# Create your tests here.

class QuestionModelTestCase(TestCase):
	def test_was_published_recently(self):
		some_time_in_the_future = timezone.now() + datetime.timedelta(days = 30)		
		q = Question(pub_date = some_time_in_the_future)
		self.assertFalse(q.was_published_recently())
