from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpRequest
from .forms import PhishingEventForm
from .models import PhishingEvent
import datetime

# Create your views here.
def index(request: HttpRequest):
    return render(request, 'index.html', None)
  
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("Success.")
        else:
            return HttpResponse("Fail")
    return render(request, 'login.html')

def report(request: HttpRequest):
    if request.method == "POST":
        form = PhishingEventForm(request.POST)
        if form.is_valid():
            form.timestamp = datetime.datetime.now()
            form.save()
            print(PhishingEvent.objects.all().values())
        else:
            print(form.errors.as_data())
        return render(request, 'report/report.html', None)
    else:
        return render(request, 'report/report.html', None)

def history(request: HttpRequest):
    data = PhishingEvent.objects.all().values()
    return render(request, 'history/history.html', {'items': data})
