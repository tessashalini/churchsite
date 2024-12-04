from django import forms
from .models import EventRequest

class EventRequestForm(forms.ModelForm):
    class Meta:
        model = EventRequest
        fields = ['title', 'email', 'event_type', 'event_date', 'description']
