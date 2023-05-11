from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Question, Answer
from .forms import QuestionForm


def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'mypet1/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'mypet1/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('mypet1:detail', question_id=question.id)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('mypet1:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'mypet1/question_form.html', context)