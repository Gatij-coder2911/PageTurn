from BookApp import views
from django.urls import path

urlpatterns = [
    path('PageTurn/',views.index, name='home'),
    path('PageTurn/register/',views.register, name='register'),
    path('PageTurn/login/', views.login, name='login')
]