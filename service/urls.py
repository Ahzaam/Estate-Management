from django.urls import path
from . import views
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home , name='home'),
    path('auth/', views.auth, name='auth'),
    path('about/', views.about, name='about'),
    path('post/user/feedback', views.feedback, name='feedback'),
    path('auth/user/register', views.register, name='register'),
    path('auth/user/login', views.login, name='login'),
    path('auth/user/logout', views.logout, name='logout'),
    path('auth/user/verify/otp', views.authotp, name='authotp'),
    path('auth/user/verify/token', views.autoLoginWithToken, name='autoLogin'),
    path('download/backup_database/please', views.download_file),
    path('myadmin/', views.myadmin),
]

# urlpatterns += staticfiles_urlpatterns()
