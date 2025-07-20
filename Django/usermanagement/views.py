from django.views.generic import TemplateView
from users.models import TenantUser, JobFunction, Language
from web_project import TemplateLayout
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from apps.phishing.models import PhishingSimulation
from django.http import JsonResponse


"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to sample/urls.py file for more pages.
"""


class UsersView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['userlist'] = TenantUser.objects.all()
        return context

class UsersAccountView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        user_id = kwargs['pk']
        userinfo = get_object_or_404(TenantUser, pk=user_id)
        context['userinfo'] = userinfo

        #Load last 15 simulations of this user
        simulations = PhishingSimulation.objects.filter(user=userinfo).order_by('-sent_at')[:15]
        context['simulations'] = simulations

        # Load job functions and languages for the dropdowns
        context['job_functions'] = JobFunction.objects.all()
        context['languages'] = Language.objects.all()
        context['users'] = TenantUser.objects.exclude(id=user_id)

        if userinfo.supervisor:
            context['supervisor'] = userinfo.supervisor
        else:
            context['supervisor'] = None

        context.update({'active_menu': 'users-overview'}) # Menu Punkt aktiv setzen
        return context

    def post(self, request, *args, **kwargs):
        user_id = kwargs['pk']
        user = get_object_or_404(TenantUser, pk=user_id)
        user.firstname = request.POST.get('modalEditUserFirstName')
        user.name = request.POST.get('modalEditUserLastName')
        user.email = request.POST.get('modalEditUserEmail')
        user.phone_number = request.POST.get('modalEditUserPhone')
        user.interface_language = request.POST.get('modalEditUserInterfaceLanguage')

        phishing_languages_codes = request.POST.getlist('modalEditUserPhishingLanguages')
        phishing_languages = Language.objects.filter(code__in=phishing_languages_codes)
        user.phishing_simulation_languages.set(phishing_languages)

        user.job_title = request.POST.get('modalEditUserJobTitle')
        job_function_id = request.POST.get('modalEditUserJobFunction')
        user.job_function = JobFunction.objects.get(id=job_function_id) if job_function_id else None

        supervisor_id = request.POST.get('modalEditUserSupervisor')
        user.supervisor = TenantUser.objects.get(id=supervisor_id) if supervisor_id else None

        try:
            user.save()
            messages.success(request, 'Daten wurden erfolgreich aktualisiert.')
        except Exception as e:
            messages.error(request, f'Ein Fehler ist aufgetreten: {e}')
        return redirect('users-account', user.id)

def phishing_simulations_data(request, user_id):
    userinfo = get_object_or_404(TenantUser, pk=user_id)
    simulations = PhishingSimulation.objects.filter(user=userinfo).order_by('-sent_at')[:10]

    data = []
    for sim in simulations:
        data.append({
            'template__id': sim.template.id,
            'template__name': sim.template.name,
            'sent_at': sim.sent_at,
            'response_time': sim.response_time,
            'completed_microtraining': sim.completed_microtraining,
            'status': sim.status
        })

    return JsonResponse({'data': data})

def UsersData(request):
    users = TenantUser.objects.values('id', 'email', 'onboarded', 'shields')
    data = []

    for user in users:
        simulations = PhishingSimulation.objects.filter(user_id=user['id']).order_by('-sent_at')[:10]
        simulation_data = []
        for sim in simulations:
            simulation_data.append(sim.status)

        user_data = {
            'id': user['id'],
            'email': user['email'],
            'shields': user['shields'],
            'onboarded': user['onboarded'],
            'simulations': simulation_data
        }

        data.append(user_data)

    return JsonResponse({'data': data})
