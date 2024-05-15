from django.contrib import admin

# Register your models here.

from .models import PhishingEvent
admin.site.register(PhishingEvent)

from .models import AnalystComment
admin.site.register(AnalystComment)
