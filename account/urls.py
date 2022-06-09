from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name='Account'),
    path('<str:id>/', views.getaccount, name='GetAccount'),
]
