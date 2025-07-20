from django.views.generic import TemplateView
from web_project import TemplateLayout
from .models import PhishingCampaign, PhishingTemplate
from .utils import replace_variables
from django.shortcuts import get_object_or_404

"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to sample/urls.py file for more pages.
"""

class PhishingView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        # Add the templates data to the context
        Phishingtemplates = PhishingTemplate.objects.all()
        context['Phishingtemplates'] = [
            {
                'id': template.id,
                'name': template.name,
                'languages': [lang.name for lang in template.languages.all()],
                'category': template.category.name,
                'difficulty_level': template.difficulty_level.name,
                'created_at': template.created_at,
                'updated_at': template.updated_at,
                'sending_email': template.sending_email,
                'sending_name': template.sending_name,
                'sending_subject': template.sending_subject,
                'content': template.content,
                'indicators_of_compromise': template.indicators_of_compromise,
            }
            for template in Phishingtemplates
        ]


        context['phishingcampaigns'] = PhishingCampaign.objects.all()
        return context

class PhishingPreviewView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        campaign_id = kwargs['pk']
        template = get_object_or_404(PhishingTemplate, pk=campaign_id)

        # Assuming the user object is available
        user = self.request.user  # Or another user object relevant for the preview

        # Replace variables in the template content
        print(user, "<<<<<<<<<<")
        sending_name = replace_variables(template.sending_name, user)
        sending_subject = replace_variables(template.sending_subject, user)
        content = replace_variables(template.content, user)

        context['Phishingtemplate'] = {
                'id': template.id,
                'name': template.name,
                'languages': [lang.name for lang in template.languages.all()],
                'category': template.category.name,
                'difficulty_level': template.difficulty_level.name,
                'created_at': template.created_at,
                'updated_at': template.updated_at,
                'sending_email': template.sending_email,
                'sending_name': sending_name,
                'sending_subject': sending_subject,
                'content': content,
                'indicators_of_compromise': template.indicators_of_compromise,
        }
        print("Returning context")

        return context
