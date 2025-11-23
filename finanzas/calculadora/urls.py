from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_calculadora, name='calculadora'),
    path('descargar_excel/', views.descarga_excel, name='descargar_excel'),  
]
