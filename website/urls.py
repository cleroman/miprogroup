from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('demande-projet/', views.demande_projet, name='demande_projet'),
]