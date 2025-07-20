from django.urls import path
from .views import DashboardView


urlpatterns = [
    path(
        "dashboard/",
        DashboardView.as_view(template_name="dashboard.html"),
        name="dashboard",
    ),
]
