from django.db import models
from member.models import EventRequest

from django.db import models

class Document(models.Model):
    CATEGORY_CHOICES = [
        ('meeting_minutes', 'Meeting Minutes'),
        ('notice', 'Notice'),
        ('agenda', 'Agenda'),
        ('announcements', 'Announcements'),
    ]

    title = models.CharField(max_length=100)
    file = models.FileField(upload_to="documents/")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Budget(models.Model):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

# models.py
from django.db import models

class Donation(models.Model):
    donor = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    verified = models.BooleanField(default=False)
    # Add other fields as necessary

    def generate_receipt(self):
        # Logic to generate a receipt
        pass


class Expense(models.Model):
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()


    def __str__(self):
        return f"Approval for {self.event.title}"


# admin_layer/models.py
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_profile')
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('member', 'Member'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.admin_profile.save()


