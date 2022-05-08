from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('momentos/', views.momentos, name='momentos'),
]
