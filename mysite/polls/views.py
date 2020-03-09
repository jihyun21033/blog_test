from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect as HRR
from django.http import HttpResponse as HR
from django.template import loader
from django.urls import reverse
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('./index.html')
    context = {'latest_question_list': latest_question_list}
    return HR(template.render(context, request))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, './results.html', {'question': question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, './detail.html', {'question' : question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        return render(request, './detail.html', {
                'question': question,
                'error_message': "You didn`t select a choice.",
                })

    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HRR(reverse('polls:results', args=(question.id,)))

# Create your views here.
