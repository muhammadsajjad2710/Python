from django.views.generic import TemplateView
from web_project import TemplateLayout
from django.contrib.auth import get_user_model


class DashboardView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        User = get_user_model()

        tenant_user_count = User.objects.count()
        # Anzahl der Benutzer, die onboarded sind
        onboarded_user_count = User.objects.filter(onboarded=True).count()
        # Prozentuale Anzahl der Benutzer, die onboarded sind
        if tenant_user_count > 0:
            onboarded_percentage = (onboarded_user_count / tenant_user_count) * 100
        else:
            onboarded_percentage = 0

        context['tenant_user_count'] = tenant_user_count
        context['onboarded_user_count'] = onboarded_user_count
        context['onboarded_percentage'] = onboarded_percentage
        return context
