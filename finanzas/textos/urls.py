from django.urls import path
from . import views

urlpatterns = [
    path('', views.textos_view, name='textos_base'),
    path('', views.textos_view, name='textos'), 
    path('pregunta/<int:pregunta_id>/', views.pregunta_detalle, name='pregunta_detalle'),
]