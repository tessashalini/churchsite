from django.db import models
from django.contrib.auth.models import User

class EventRequest(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()  # This field should exist
    # time = models.TimeField()  # This field should exist
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')
    
    def save(self, *args, **kwargs):
        if self.status == 'Approved':
            if EventRequest.objects.filter(date=self.date, status='Approved').exists():
                raise ValidationError('An event is already approved for this date.')
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title



from django.db import models

from django.db import models

class Donation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Ensure this field exists
    transfer_method = models.CharField(max_length=50)
    receipt = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    donation_purpose = models.TextField()
    receipt_file = models.FileField(upload_to='receipts/')

    def __str__(self):
        return f"Donation by {self.name} on {self.submitted_at}"

# member/models.py

from django.db import models

class CommunityMessage(models.Model):
    username = models.CharField(max_length=255)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}: {self.message[:50]}"
