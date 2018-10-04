from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Question, Choice


def index(request):
    # Question클래스에 대한 QuerySet을 가져옴
    #  게시일자 속성에 대한 내림차순 순서로 최대 5개까지
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')
    question = get_object_or_404(Question, pk=question_id)

    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    # question_id에 해당하는 Question인스턴스를 render함수의 context로 전달
    # template은 'polls/results.html'을 사용

    # 1. Template에서는 전달받은 Question인스턴스에 속하는 Choice목록을 순회하며 보여줌
    #  이 때, 각 Choice아이템들의 'choice_text' 및 'votes'속성 값도 같이 출력

    # 2. 'Return to polls index'링크 만들기 (polls.views.index로 돌아가면 됨)
    context = {
        'question': get_object_or_404(Question, pk=question_id),

    }
    return render(request, 'polls/results.html', context)


def vote(request, question_id):
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
