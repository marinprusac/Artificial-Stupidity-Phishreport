from django.contrib import admin

# Register your models here.

from .models import PhishingEventModel
admin.site.register(PhishingEventModel)

from .models import AnalystCommentModel
admin.site.register(AnalystCommentModel)
