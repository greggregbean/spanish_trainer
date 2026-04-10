from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('topics/', views.topic_list, name='topics'),
    path('topics/<int:topic_id>/', views.cards_by_topic, name='cards'),
    path('add/', views.add_card, name='add_card'),
    path('quiz/', views.quiz, name='quiz'),
]