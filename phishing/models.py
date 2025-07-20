from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class PhishingCampaign(models.Model):
    # Basic attributes
    name = models.CharField(max_length=255)
    languages = models.JSONField(default=list)  # Stores supported languages
    category = models.IntegerField()
    difficulty_level = models.IntegerField()

    # Email related fields
    sending_email_address = models.EmailField()
    sending_email_name = models.CharField(max_length=255)
    sending_subject = models.CharField(max_length=255)

    # Template content
    content = models.TextField()

    # Timestamps and user information (only for custom templates)
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    modification_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# models.py

class PhishingCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class PhishingDifficultyLevel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Indicator(models.Model):
    INDICATOR_TYPE_CHOICES = [
        ('sender', 'Sender'),
        ('subject', 'Subject'),
        ('content', 'Content'),
        ('link', 'Link'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    indicator_type = models.CharField(max_length=50, choices=INDICATOR_TYPE_CHOICES)

    def __str__(self):
        return self.name

class PhishingTemplate(models.Model):
    name = models.CharField(max_length=255)
    languages = models.ManyToManyField(Language)
    category = models.ForeignKey(PhishingCategory, on_delete=models.CASCADE)
    difficulty_level = models.ForeignKey(PhishingDifficultyLevel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    sending_email = models.EmailField()
    sending_name = models.CharField(max_length=255)
    sending_subject = models.CharField(max_length=255)
    content = models.TextField()
    indicators_of_compromise = models.ManyToManyField(Indicator)

    def __str__(self):
        return self.name

class PhishingSimulation(models.Model):
    template = models.ForeignKey(PhishingTemplate, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    responded = models.BooleanField(default=False)
    response_time = models.DateTimeField(null=True, blank=True)
    clicked_link = models.BooleanField(default=False)
    completed_microtraining = models.BooleanField(default=False)

    @property
    def status(self):
        if self.clicked_link:
            return 'Failed'
        elif self.responded:
            return 'Success'
        else:
            return 'In Progress'

    def __str__(self):
        return f"{self.user} - {self.template.name} - {self.sent_at}"

class Gif(models.Model):
    gif_id = models.CharField(max_length=50)
    gif_type = models.CharField(max_length=20, choices=[('success', 'Success'), ('failed', 'Failed')])

    def __str__(self):
        return f"{self.gif_type} - {self.gif_id}"
