from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('meeting_minutes', 'Meeting Minutes'),
        ('notice', 'Notice'),
        ('agenda', 'Agenda'),
        ('announcements', 'Announcements'),
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES)

    class Meta:
        model = Document
        fields = ['title', 'file', 'category']
