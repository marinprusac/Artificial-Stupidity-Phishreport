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

