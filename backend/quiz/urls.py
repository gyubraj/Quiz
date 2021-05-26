from django.urls import path
from .views import quizView
urlpatterns=[
   path('',quizView,name='addQuestion')
]