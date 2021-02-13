from django.shortcuts import render

from .forms import MyForm1
from .models import Question, Answer, AdvUser


def temp_page(request):
    return render(request, 'test_app/add_question_form.html')


def index(request):
    return render(request, 'test_app/index.html')


def my_view1(request):
    user = AdvUser.objects.get(id=1)
    if request.method == 'POST':
        form = MyForm1(request.POST, answers_cnt=request.POST.get('answer_block_count'))
        if form.is_valid():
            answer_list = request.POST.get('answer_list')
            if answer_list:
                answer_list = [int(val) for val in answer_list.split(',')]

            question = Question()
            question.question = request.POST.get('question')
            question.single_answer = 1 if request.POST.get('single_answer') else 0
            question.is_active = 1 if request.POST.get('is_active') else 0
            question.author = user
            question.save()
            print(answer_list)
            for i in range(len(answer_list)):
                answer = Answer()
                answer.question = question
                answer.author = user
                answer.answer = request.POST.get('answer_text_{}'.format(answer_list[i]))
                answer.is_active = 1 if request.POST.get('answer_is_active_{}'.format(answer_list[i])) else 0
                answer.correct = 1 if request.POST.get('answer_is_correct_{}'.format(answer_list[i])) else 0
                answer.save()
            form = MyForm1()
        else:
            print('not valid!')
    else:
        form = MyForm1()

    return render(request, 'test_app/add_question_form.html', {'form': form})
