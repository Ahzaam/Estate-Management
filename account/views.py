from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from service. models import Users
from django.contrib.auth.hashers import check_password
# Create your views here.

def account(request):
    if request.session.get('authenticated'):
        userid = request.session.get('userid')
        return redirect(f'/account/{userid}')
    else:
        return redirect('/auth')
    del userid

def myaccount(request, id):
    if request.session.get('userid') == id:
        data = Users.objects.get(uuid=id)
        name = data.name
        return render(request, 'account/home.html', {'id': id, 'name': name})
    elif Users.objects.filter(uuid=id).exists():
        email = Users.objects.get(uuid=id).email

        return render(request, 'account/confirm.html', {'email': email})
    else:
        return redirect('sorry/user.not.found')


def accountlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email , 'ewuhiug')
        if Users.objects.filter(email=email).exists():
            data = Users.objects.get(email=email)

            if check_password(request.POST.get('password'), data.password):
                request.session['authenticated'] = True
                request.session['userid'] = data.uuid
                return JsonResponse({'status': 200}, status=200)

            else:
                return JsonResponse({'status': 401}, status=201)
        else:
            return JsonResponse({'status': 204}, status=400)
    else:
        return JsonResponse({'status': 400}, status=400)

    del email, data, token



def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
