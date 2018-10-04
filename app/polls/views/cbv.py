# polls.vews.cbv(class-based view)
from django.views import generic

from ..models import Question


class IndexView(generic.ListView):
    model = Question
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    ordering = ('-pub_date',)

    def get_queryset(self):
        return super().get_queryset()[:5]
