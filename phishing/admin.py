
# Register your models here.
from django.contrib import admin
from .models import PhishingCampaign, PhishingTemplate, PhishingSimulation, Gif


@admin.register(PhishingCampaign)
class PhishingCampaignAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'difficulty_level', 'sending_email_address']
    list_filter = ['languages', 'category', 'difficulty_level']
    search_fields = ['name', 'content']


admin.site.register(PhishingTemplate)
admin.site.register(PhishingSimulation)
admin.site.register(Gif)
