from django.db import models
from django.contrib.auth.models import User

class EventRequest(models.Model):
    EVENT_TYPES = [
        ('wedding', 'Wedding'),
        ('baptism', 'Baptism'),
        ('birthday', 'Birthday Thanksgiving'),
        ('funeral', 'Funeral'),
        ('first-communion', 'First Communion'),
        ('new-parish', 'New Parish'),
    ]

    title = models.CharField(max_length=100)  # Event title
    email = models.EmailField()  # Requester's email
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)  # Type of event
    event_date = models.DateField()  # Requested date
    description = models.TextField(blank=True, null=True)  # Optional description
    member = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user requesting
    is_approved = models.BooleanField(default=False)  # Approved or not

    created_at = models.DateTimeField(auto_now_add=True)  # When the request was created

    def __str__(self):
        return self.title
