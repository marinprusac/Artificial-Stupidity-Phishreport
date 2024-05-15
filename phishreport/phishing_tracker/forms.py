from django import forms
from .models import PhishingEvent

class PhishingEventForm(forms.ModelForm):
    class Meta:
        model = PhishingEvent
        fields = ['name', 'affected_brand', 'description', 'malicious_campaign_url', 'list_of_matching_keywords']