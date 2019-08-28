from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('submitotp/', views.submitotp, name='submitotp'),
    path('initotp/', views.initotp, name='initotp'),
    path('simulator/', views.simulator, name='simulator'),
    path('termurl/', views.termurl, name='termurl')

]