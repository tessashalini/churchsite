# forms.py

from django import forms
from .models import ContactSubmission

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['full_name', 'phone', 'email', 'subject', 'question']

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import SignUpCode  # Ensure you have this model defined

class CustomUserCreationForm(UserCreationForm):
    extra_code = forms.CharField(max_length=10, required=True, help_text='Enter the code provided by the admin.')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'extra_code')

    def clean_extra_code(self):
        code = self.cleaned_data.get('extra_code')
        try:
            signup_code = SignUpCode.objects.get(code=code, is_used=False)
        except SignUpCode.DoesNotExist:
            raise forms.ValidationError("Invalid or already used code.")
        return code

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Mark the code as used
            SignUpCode.objects.filter(code=self.cleaned_data['extra_code']).update(is_used=True)
        return user
