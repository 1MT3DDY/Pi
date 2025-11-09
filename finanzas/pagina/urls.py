from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('statichastaqcambienvideos/', views.videos_view, name='videos'),
    path('logout/', views.logout_view, name='logout'),
]