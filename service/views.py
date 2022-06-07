from django.shortcuts import render
from django.http import JsonResponse
from . models import Feedback




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
