from django.shortcuts import render
from django.http import JsonResponse
from . models import Feedback, tempUser, Users


# Mail Settings
from django.conf import settings
from django.core.mail import send_mail
import random


# Create your views here.

def home(request):
    return render(request, 'home.html')

def auth(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def feedback(request):
    if  request.method == "GET":
        Feedback.objects.create(feedback=str(request.GET.get('feedback')))

        return JsonResponse({'success': 'Feedback Added'}, status=200)
    else: return JsonResponse({'success': 'Some thing went wrong. Refresh your page'}, status=400)

def login(request):
    return 0



def register(request):
    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')

        request.session['email'] = email
        request.session['name'] = name

        if Users.objects.filter(email=email).exists():
            del email, name, request.session['name'],request.session['email']

            return JsonResponse({'status': 226}, status=226)

        else:
            otp = random.randint(12423, 99999)
            request.session['otp'] = otp

            subject = 'GLiDE Ceylon Verification'
            message = f'Hi {name}, Your GLiDE Ceylon verication code is. \nCode: {otp}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]

            tempUser.objects.create(otp=otp, name=name, email=email, password=request.POST.get('regpassword'), city=request.POST.get('city'), state=request.POST.get('state'))

            send_mail( subject, message , email_from, recipient_list )

            del email
            del name
            del otp

            return JsonResponse({'status': 202}, status=202)

    return JsonResponse({'status': 'Bad Request'}, status=404)


def authotp(request):
    if request.method == 'POST':
        sesOtp = int(request.session['otp'])
        print(sesOtp)
        print(request.POST.get('otp'))

        if sesOtp == int(request.POST.get('otp')):

            tempUserData = tempUser.objects.get(otp=request.session['otp'])
            tempUser.objects.get(otp=request.session['otp']).delete()
            Users.objects.create(name=tempUserData.name, email=tempUserData.email, password=tempUserData.password, city=tempUserData.city, state=tempUserData.state)
            name = request.session['name']
            subject = 'Welcome to GLiDE Ceylon'
            message = f'Thanks {name},\nYour Successfully Created acount in GLiDE Ceylon\n '
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [ request.session['email'], 'fawmeeahzam123@gmail.com']

            send_mail( subject, message , email_from, recipient_list )

            del request.session['otp']
            del request.session['name']
            del request.session['email']
            del name
            del tempUserData

            return JsonResponse({'status': 200}, status=200)
        return JsonResponse({'status': 400}, status=400)
    return JsonResponse({'status': 404}, status=404)
