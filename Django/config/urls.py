"""
URL configuration for web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from web_project.views import SystemView

# for addin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # starter urls
    path("", include("apps.sample.urls")),
    # Dashboard urls
    path("", include("apps.dashboard.urls")),
    # pages urls
    path("", include("apps.pages.urls")),
	# phishing urls
    path("", include("apps.phishing.urls")),
	# users urls
    path("", include("apps.usermanagement.urls")),
    # Settings Manager urls
    path("", include("apps.settingsmanager.urls")),
    # microtraining urls
    path("", include("apps.microtraining.urls")),
    # Game urls
    path("", include("apps.game.urls")),
    # User Reporting Spam urls
    path("", include("apps.reportingspam.urls")),
    # auth urls
    path("", include("auth.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = SystemView.as_view(template_name="pages_misc_error.html", status=404)
handler403 = SystemView.as_view(template_name="pages_misc_not_authorized.html", status=403)
handler400 = SystemView.as_view(template_name="pages_misc_error.html", status=400)
handler500 = SystemView.as_view(template_name="pages_misc_error.html", status=500)
