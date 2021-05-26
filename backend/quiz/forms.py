from django import forms
from .models import language_choices,level_choices
from django.contrib.auth.models import User
class QuizForm(forms.Form):
    answer_choice=(
        ('choice1','option1'),
        ('choice2','option2'),
        ('choice3','option3'),
        ('choice4','option4')
    )
    question=forms.CharField(label="Enter Quiz Question",max_length=255)
    language=forms.ChoiceField(choices=language_choices,label="Choose Language")
    level=forms.ChoiceField(choices=level_choices,label="Choose Level")
    choice1=forms.CharField(label="Option 1",max_length=255)
    choice2 = forms.CharField(label="Option 2", max_length=255)
    choice3 = forms.CharField(label="Option 3", max_length=255)
    choice4 = forms.CharField(label="Option 4", max_length=255)
    answer=forms.ChoiceField(label="Choose Answer",choices=answer_choice)

class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','password')
        widgets={
            'password':forms.TextInput(attrs={
                'type':'password'
            })
        }
        labels={
            "username":"Enter Username",
            "password":'Enter Password'
        }