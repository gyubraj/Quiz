from django.urls import path
from .views import Quiz
urlpatterns=[
    path('quiz',Quiz.as_view())
]