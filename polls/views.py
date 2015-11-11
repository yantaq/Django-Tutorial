from django.shortcuts import get_object_or_404, render
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of quesiton %s."
    return render(response % question_id)

def vote(request, question_id):
    return render(request, "You're voting on quesiton %s." % question_id)