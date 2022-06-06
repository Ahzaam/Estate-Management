from django.urls import path
from . import views
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home , name='home'),
    path('auth/', views.auth, name='auth'),
    path('about/', views.about, name='about'),
]

# urlpatterns += staticfiles_urlpatterns()
