import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        # 미래의 datetime객체를 time변수에 할당
        time = timezone.now() + datetime.timedelta(days=30)
        # 새 Question인스턴스를 생성, pub_date값에 미래시간을 주어줌
        future_question = Question(pub_date=time)
        # 주어진 2개의 객체가 같아야 할 것(is)으로 기대함
        #  같지 않으면 실패
        self.assertIs(
            future_question.was_published_recently(),
            False,
        )
