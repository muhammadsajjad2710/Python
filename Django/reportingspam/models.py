from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ReportingSpam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reportingspam')
    reported_at = models.DateTimeField(auto_now_add=True)
    clicked_link = models.BooleanField(default=False)
    credentials_entered = models.BooleanField(default=False)
    mail_header = models.TextField()
    mail_content = models.TextField()
    subject = models.CharField(max_length=255)
    sender = models.CharField(max_length=255)
    links = models.TextField(help_text="Alle separierten Links, durch Kommas getrennt.")
    sender_ip = models.GenericIPAddressField(blank=True, null=True)

    def __str__(self):
        return f"SPAM Report {self.id} by {self.user.username} on {self.reported_at}"
