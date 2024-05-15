from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .forms import PhishingEventForm
from .models import PhishingEvent
import datetime

# Create your views here.
def index(request: HttpRequest):
    return render(request, 'index.html', None)

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