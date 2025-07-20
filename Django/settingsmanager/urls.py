from django.urls import path
from .views import SettingsManagerCompanyView, SettingsManagerGeneralView, SettingsManagerLeaderboardView


urlpatterns = [
    path(
        "settings/company",
        SettingsManagerCompanyView.as_view(template_name="settings_company.html"),
        name="settings-company",
    ),
    path(
        "settings/general",
        SettingsManagerGeneralView.as_view(template_name="phishing_overview.html"),
        name="phishing_overview",
    ),
    path(
        "settings/training",
        SettingsManagerLeaderboardView.as_view(template_name="settings_training.html"),
        name="settings-training",
    ),
    path(
        "settings/leaderboard",
        SettingsManagerLeaderboardView.as_view(template_name="settings_leaderboard.html"),
        name="settings-leaderboard",
    ),
]
