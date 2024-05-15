from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def index(request: HttpRequest):
    return render(request, 'index.html', None)

def report(request: HttpRequest):
    if request.method == "POST":
        pass
        return render(request, 'report/report.html', None)
    else:
        return render(request, 'report/report.html', None)