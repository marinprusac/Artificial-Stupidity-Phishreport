from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html', None)

def report(request):
    return render(request, 'report/report.html', None)