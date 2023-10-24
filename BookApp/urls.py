from BookApp import views
from django.urls import path

urlpatterns = [
    path('PageTurn/',views.index, name='home'),
    path('PageTurn/Register/',views.register, name='register'),
    path('PageTurn/Login/', views.login, name='login'),
    path('PageTurn/WhyUse/', views.whyuse, name='whyuse'),
    path('PageTurn/MostlyBought/', views.mostlybought, name='mostlybought'),
    path('PageTurn/AboutUs/', views.aboutus, name='aboutus'),
    path('PageTurn/TermsConditions/', views.termsconditions, name='termsconditions'),
    path('PageTurn/PrivacyPolicy/', views.privacypolicy, name='privacypolicy'),
    path('PageTurn/SafetyTips/', views.safetytips, name='safetytips'),
    path('PageTurn/Helpline/', views.helpline, name='helpline'),
    path('PageTurn/SellBooks/', views.sellbooks, name='sellbooks')
]