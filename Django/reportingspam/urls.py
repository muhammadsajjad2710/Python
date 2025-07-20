from django.urls import path
from .views import report_spam, ReportingSpamView, get_email_data


urlpatterns = [
    path(
        "report_spam/",
		report_spam,
        name="report-spam",
    ),
    path(
        "userreports/",
        ReportingSpamView.as_view(template_name="userreports.html"),
        name="userreports",
    ),
    path(
        "emails/data/<int:email_id>/",
        get_email_data,
        name="email-data",
    ),
]
