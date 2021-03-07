from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('newDoctor/', views.newDoctor, name='newDoctor'),
    path('newPatient/', views.newPatient, name='newpatient'),
    path('seeUser/', views.seeUser, name='seeUser'),
    path('giveAdvice/', views.giveAdvice, name='giveAdvice'),
    path('readSuggestion/', views.readSuggestion, name='readSuggestion'),
]