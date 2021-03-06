from django.urls import path
from . import views

urlpatterns = [
    path('line-chart/', views.line_chart, name='line-chart'),
]