from django.db import models

class ContactSubmission(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    question = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.subject}"

from django.db import models

class SignUpCode(models.Model):
    code = models.CharField(max_length=10, unique=True)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return self.code

