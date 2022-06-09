from django.shortcuts import render, redirect
from django.http import JsonResponse
from . models import Feedback, tempUser, Users, AutoLoginToken
import uuid

from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.sites.shortcuts import get_current_site

# Mail Settings
from django.conf import settings
from django.core.mail import send_mail
import random


# Create your views here.

def home(request):
    return render(request, 'service/home.html')

def auth(request):
    return render(request, 'service/login.html')

def about(request):
    return render(request, 'service/about.html')

def feedback(request):
    if  request.method == "GET":
        Feedback.objects.create(feedback=str(request.GET.get('feedback')))

        return JsonResponse({'success': 'Feedback Added'}, status=200)
    else: return JsonResponse({'success': 'Some thing went wrong. Refresh your page'}, status=400)

def login(request):


    if request.method == 'POST':
        email = request.POST.get('email')

        if Users.objects.filter(email=email).exists():
            data = Users.objects.get(email=email)

            if check_password(request.POST.get('password'), data.password):
                token = uuid.uuid4()
                AutoLoginToken.objects.create(token=token, email=email, name=data.name)
                return JsonResponse({'status': 200, 'name':data.name, 'email': email, 'token': token}, status=200)

            else:
                return JsonResponse({'status': 401}, status=201)
        else:
            return JsonResponse({'status': 204}, status=201)
    return JsonResponse({'status': 400}, status=400)

    del email, data, token




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

            password = make_password(tempUserData.password)

            useruuid = uuid.uuid4()

            Users.objects.create(name=tempUserData.name, email=tempUserData.email, password=password, city=tempUserData.city, state=tempUserData.state, uuid=useruuid)
            name = request.session['name']
            subject = 'Welcome to GLiDE Ceylon'
            message = f'Thanks {name},\nYour Successfully Created acount in GLiDE Ceylon\nyour account will be available at \nhttps://{get_current_site(request).domain}/account/{useruuid}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [ request.session['email'], 'fawmeeahzam123@gmail.com']


            send_mail( subject, message , email_from, recipient_list )

            del request.session['otp']
            del request.session['name']
            del request.session['email']
            del name, useruuid
            del tempUserData

            return JsonResponse({'status': 200}, status=200)
        return JsonResponse({'status': 400}, status=400)
    return JsonResponse({'status': 404}, status=404)


def autoLoginWithToken(request):
    token = request.POST.get('token')
    if AutoLoginToken.objects.filter(token=token).exists():
        data = AutoLoginToken.objects.get(token=token)
        email = data.email
        name = data.name
        return JsonResponse({'status': 200, 'name': name, 'email': email}, status=200)
    else:
        return JsonResponse({'status': 404}, status=201)

    del data, email, name, token


def logout(request):
    if request.method == 'GET':
        token = request.GET.get('token')
        if AutoLoginToken.objects.filter(token=token).exists():
            AutoLoginToken.objects.get(token=token).delete()
            print('Deleted token')
            return redirect('/')
        else:
            print('Does not exist')
            return redirect('/')
            return JsonResponse({'status': 404}, status=404)
    else: return JsonResponse({'status': 404}, status=404)
