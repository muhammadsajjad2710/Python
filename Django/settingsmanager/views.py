from django.views.generic import TemplateView
from web_project import TemplateLayout
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import SettingsCompany, SettingsLeaderboard

# Create your views here.
class SettingsManagerCompanyView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        current_tenant = self.request.tenant
        settings, created = SettingsCompany.objects.get_or_create(tenant=current_tenant)
        context['settings'] = settings
        return context

    def post(self, request):
        current_tenant = request.tenant
        settings, created = SettingsCompany.objects.get_or_create(tenant=current_tenant)
        settings.company_name = request.POST.get('companyname')
        settings.address = request.POST.get('address')
        settings.zipcode = request.POST.get('zipcode')
        settings.city = request.POST.get('city')
        settings.website = request.POST.get('website', '')
        settings.brand_color = request.POST.get('brand_color', '#FFFFFF')  # Standardwert als Weiß
        try:
            settings.save()
            messages.success(request, 'Daten wurden erfolgreich aktualisiert.')
        except Exception as e:
            messages.error(request, f'Ein Fehler ist aufgetreten: {e}')
        return redirect('settings-company')

class SettingsManagerGeneralView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context

class SettingsManagerLeaderboardView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        current_tenant = self.request.tenant
        settings, created = SettingsLeaderboard.objects.get_or_create(tenant=current_tenant)
        context['leaderboard_settings'] = settings
        return context

    def post(self, request, *args, **kwargs):
        current_tenant = request.tenant
        settings, created = SettingsLeaderboard.objects.get_or_create(tenant=current_tenant)
        settings.active = request.POST.get('leaderboard_active') == 'on'
        settings.group_by = request.POST.get('leaderboard_groupby', settings.group_by)
        settings.privacy_default = request.POST.get('leaderboard_privacy_default') == 'on'
        settings.privacy_user_control = request.POST.get('leaderboard_privacy_user') == 'on'
        try:
            settings.save()
            messages.success(request, 'Leaderboard-Einstellungen wurden erfolgreich aktualisiert.')
        except Exception as e:
            messages.error(request, f'Ein Fehler ist aufgetreten: {e}')
        return redirect('settings-leaderboard')
