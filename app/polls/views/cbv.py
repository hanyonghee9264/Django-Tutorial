# polls.vews.cbv(class-based view)
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.views import generic, View

from ..models import Question, Choice


class IndexView(generic.ListView):
    model = Question
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    ordering = ('-pub_date',)

    def get_queryset(self):
        return super().get_queryset().filter(pub_date__lte=timezone.now())[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    pk_url_kwarg = 'question_id'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    pk_url_kwarg = 'question_id'


class VoteView(View):
    def post(self, request, question_id):
        # question_id가 pk인 Question객체를 DB로부터 가져와 데이터로 생성
        # 만약 해당하는 Question이 없다면 Http404예외가 발생함
        question = get_object_or_404(Question, pk=question_id)
        try:
            # 현재 투표중인 Question에 속한 Choice목록에서
            # pk가 POST요청에 전달된 'choice'값에 해당하는 Choice객체를 selected_choice변수에 할당
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            # 위의 try문에서 발생할 수 있는 예외는 2가지
            # 1. KeyError:
            #     request.POST에 'choice'키가 없을 때 발생
            # 2. Choice.DoesNotExist:
            #     question.choice_set.get(pk=무언가)에서 발생 (pk에 해당하는 객체가 DB에 없을 경우)
            context = {
                'question': question,
                'error_message': "You didn't select a choice.",
            }
            return render(request, 'polls/detail.html', context)
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return redirect('polls:results', question_id)