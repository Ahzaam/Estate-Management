from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name='Account'),
    path('<str:id>/', views.myaccount, name='GetAccount'),
    path('id/confirm/password', views.accountlogin, name='Account')
]
