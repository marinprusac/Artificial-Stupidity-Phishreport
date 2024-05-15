from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpRequest
from .forms import PhishingEventForm
from .models import PhishingEvent
import datetime
from django.contrib.auth.models import User
from django.contrib import messages

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
            form.save()
            username = request.POST.get("eventNameInput")
            brand = request.POST.get("eventBrandInput")
            malicious_url = request.POST.get("maliciousUrlInput")
            desc = request.POST.get("eventDescriptionTextArea")
            keywords = request.POST.get("eventKeywordsTextArea")
            timedate = datetime.datetime.now()

            event = PhishingEvent(
                name=username,
                affected_brand=brand,
                malicious_campaign_url=malicious_url,
                timestamp=timedate,
                list_of_matching_keywords=keywords,
                description=desc,
                status="TODO"
            )
            event.save()
        return render(request, 'report/report.html', None)
    else:
        return render(request, 'report/report.html', None)

def register(request: HttpRequest):
    if request.method == "GET":
        return render(request, 'register.html', None)
    elif request.method != "POST":
        return HttpResponse("Unsupported HTTP Method.")
    name = request.POST["name"]
    surname = request.POST["sname"]
    email = request.POST["email"]
    password = request.POST["pass"]
    if len(password) < 8:
        messages.error(request, "Password should be at least 8 characters long.")
        return render(request, "register.html")
    user = User.objects.create_user(first_name=name, last_name=surname, email=email, password=password)
    user.save()
    return redirect("login")