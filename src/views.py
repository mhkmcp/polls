from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question, Choice



def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'question_list': question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context)


def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/result.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            'question': question,
            'error_message': 'You did not select a choice'
        }
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('result', question_id)

