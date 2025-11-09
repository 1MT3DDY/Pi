from django.urls import path
from . import views

urlpatterns = [
    path('', views.textos_view, name='textos_base'),
    # Usaremos esta línea para que al entrar a /textos/ cargue la función textos_view
    path('', views.textos_view, name='textos'), 
    path('pregunta/<int:pregunta_id>/', views.pregunta_detalle, name='pregunta_detalle'),
]