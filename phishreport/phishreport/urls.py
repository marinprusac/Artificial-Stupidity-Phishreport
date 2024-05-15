"""
URL configuration for phishreport project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from phishing_tracker import views
from . import settings
from django.contrib import admin
from phishing_tracker.views import index, report, history

urlpatterns = [
    path('', index, name='index'),
    path('history', history, name='history'),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path(settings.LOGIN_URL, views.login_view, name='login'),
    path('register/', views.register, name="register"),
    path('report', report, name='report'),
]
