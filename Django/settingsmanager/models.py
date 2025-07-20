from django.db import models
from apps.microtraining.models import MicroTrainingCategory, MicroTraining


class SettingsCompany(models.Model):
    tenant = models.OneToOneField('customers.Client', on_delete=models.CASCADE, related_name='settings_company')
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    brand_color = models.CharField(max_length=7, default='#FFFFFF')

    def __str__(self):
        return self.company_name

class SettingsLeaderboard(models.Model):
    tenant = models.ForeignKey('customers.Client', on_delete=models.CASCADE, related_name='settings_leaderboard')
    active = models.BooleanField(default=False)
    group_by = models.CharField(max_length=100, default="department")
    privacy_default = models.BooleanField(default=True)
    privacy_user_control = models.BooleanField(default=True)

class Settings(models.Model):
    company_name = models.CharField(max_length=255)
    company_address = models.CharField(max_length=255)
    company_postal_code = models.CharField(max_length=8)
    company_city = models.CharField(max_length=100)
    company_country = models.CharField(max_length=100)
    company_phone_number = models.CharField(max_length=20)
    company_website = models.URLField()
    leaderboard_enable = models.BooleanField(default=True)
    leaderboard_default_anonymous = models.BooleanField(default=False)
    leaderboard_groupby = models.IntegerField(default=1)
    leaderboard_duration = models.IntegerField(default=3)

    def __str__(self):
        return self.company_name

class MicrotrainingCategoryActivation(models.Model):
    category = models.ForeignKey(MicroTrainingCategory, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.category.name

class MicrotrainingTrainingActivation(models.Model):
    training = models.ForeignKey(MicroTraining, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.training.name
