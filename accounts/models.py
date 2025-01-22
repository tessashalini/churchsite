from django.db import models

class SignUpCode(models.Model):
    code = models.CharField(max_length=10, unique=True)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return self.code
from django.contrib.auth.models import User
from django.db import models

# accounts/models.py
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='accounts_profile')
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('member', 'Member'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

