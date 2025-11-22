from django.urls import path
from . import views

urlpatterns = [
    # La ruta base ahora muestra la portada/confirmación
    path('', views.quiz_landing, name='quiz'),
    
    # Esta ruta ejecuta el inicio (y borrado de datos antiguos)
    path('iniciar/', views.quiz_start, name='quiz_start'),
    
    path('question/<int:idx>/', views.quiz_question, name='quiz_question'),
    path('submit/', views.quiz_submit, name='quiz_submit'),
]