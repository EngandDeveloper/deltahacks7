from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='home'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('loginUser/', views.loginUser, name='loginUser'),
    path('logoutUser/', views.logoutUser, name='logoutUser'),
    path('registerUser/', views.registerUser, name='registerUser'),
]