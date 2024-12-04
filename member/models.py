

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class EventRequest(models.Model):
    member = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="member_event_requests"  # Add a unique related_name
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    event_date = models.DateField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title


