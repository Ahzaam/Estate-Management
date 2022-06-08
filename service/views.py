from django.shortcuts import render
from django.http import JsonResponse
from . models import Feedback


# Mail Settings
from django.conf import settings
from django.core.mail import send_mail



# Create your views here.

def home(request):
    return render(request, 'home.html')

def auth(request):
    subject = 'welcome to GC'
    message = 'Hi, thank you for registering in Glide Ceylon.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['fawmeeahzam123@gmail.com' ]
    send_mail( subject, message, email_from, recipient_list )

    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def feedback(request):
    if  request.method == "GET":
        Feedback.objects.create(feedback=str(request.GET.get('feedback')))

        return JsonResponse({'success': 'Feedback Added'}, status=200)
    else: return JsonResponse({'success': 'Some thing went wrong. Refresh your page'}, status=400)
