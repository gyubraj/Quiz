from django.shortcuts import render, redirect
from .forms import QuizForm
from django.contrib import messages
from .models import Question,Answer,Choice

def quizView(request):
    if request.method=="GET":
        form=QuizForm()
        context={
            'form':form
        }
        return render(request,'quiz.html',context)
    else:
        form=QuizForm(request.POST)
        if form.is_valid():
            question=form.cleaned_data.get('question')
            language=form.cleaned_data.get('language')
            level=form.cleaned_data.get('level')
            try:
                questionCheck=Question.objects.get(question__iexact=question)
                context = {
                    'form': form
                }
                messages.error(request,"Question already exist.")
                return render(request, 'quiz.html', context)
            except:
                questionObject=Question.objects.create(
                    question=question,
                    language=language,
                    level=level
                )
                choice1=form.cleaned_data.get('choice1')
                choice2 = form.cleaned_data.get('choice2')
                choice3 = form.cleaned_data.get('choice3')
                choice4 = form.cleaned_data.get('choice4')
                choice1Object=Choice.objects.create(
                    question=questionObject,
                    choice=choice1
                )
                choice2Object = Choice.objects.create(
                    question=questionObject,
                    choice=choice2
                )
                choice3Object = Choice.objects.create(
                    question=questionObject,
                    choice=choice3
                )
                choice4Object = Choice.objects.create(
                    question=questionObject,
                    choice=choice4
                )
                answerChoiceObject=Choice.objects.filter(
                    choice__iexact=form.cleaned_data.get(form.cleaned_data.get('answer'))
                ).last()
                answerObject=Answer.objects.create(
                    question=questionObject,
                    answer=answerChoiceObject
                )
                messages.success(request,"Question added successfully.")
                return redirect('addQuestion')
