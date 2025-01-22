from django import forms
from .models import EventRequest
from .models import Donation

class EventRequestForm(forms.ModelForm):
    class Meta:
        model = EventRequest
        fields = ['title', 'description', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['name', 'email', 'phone', 'amount', 'transfer_method', 'receipt', 'donation_purpose', 'receipt_file']
    amount = forms.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        required=True, 
        min_value=0.00,  # Ensure amount is not below 0.00
        widget=forms.NumberInput(attrs={'placeholder': 'Enter donation amount'})
    )
    transfer_method = forms.ChoiceField(
        choices=[
            ('online-payment', 'Online Payment'),
            ('bank-transfer', 'Bank Transfer'),
            ('cash', 'Cash'),
            ('cheque', 'Cheque')
        ],
        initial='online-payment',
        disabled=False  # Keep the field disabled
    )
    receipt = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], initial='yes')
    receipt_file = forms.FileField(required=True)

    def __init__(self, *args, **kwargs):
        super(DonationForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Your full name'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Your email address'})
        self.fields['phone'].widget.attrs.update({'placeholder': 'Your phone number'})
        self.fields['donation_purpose'].widget.attrs.update({'placeholder': 'What is your donation for?'})

# member/forms.py

from django import forms
from .models import CommunityMessage

class CommunityMessageForm(forms.ModelForm):
    class Meta:
        model = CommunityMessage
        fields = ['username', 'message']
