from django.urls import path
from .views import quizView,loginView
urlpatterns=[
   path('',quizView,name='addQuestion'),
   path('/login',loginView,name='login')
]