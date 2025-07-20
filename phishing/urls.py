from django.urls import path
from .views import PhishingView, PhishingPreviewView


urlpatterns = [
    path(
        "phishing/",
        PhishingView.as_view(template_name="phishing_overview.html"),
        name="phishing-overview",
    ),
    path(
        "phishing/preview/<int:pk>/",
        PhishingPreviewView.as_view(template_name="phishing_preview.html"),
        name="phishing-preview",
    ),
]
