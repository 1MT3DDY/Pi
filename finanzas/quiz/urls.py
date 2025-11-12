from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_start, name='quiz'),
    path('question/<int:idx>/', views.quiz_question, name='quiz_question'),
    path('submit/', views.quiz_submit, name='quiz_submit'),
]