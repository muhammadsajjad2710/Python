from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.generic import TemplateView
from web_project import TemplateLayout
from .models import ReportingSpam
from django.urls import reverse_lazy
import re
from django.shortcuts import get_object_or_404

class ReportingSpamView(TemplateView):

    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['reports'] = ReportingSpam.objects.all().order_by('-reported_at')
        return context

def get_email_data(request, email_id):
    email = get_object_or_404(ReportingSpam, pk=email_id)
    data = {
        'subject': email.subject,
        'sender': email.sender,
        'content': email.mail_content,
        'header': email.mail_header,
        'links': email.links,
        'sender_ip': email.sender_ip,
        'reported_at': email.reported_at.strftime("%Y-%m-%d %H:%M")
    }
    return JsonResponse(data)


@csrf_exempt
def report_spam(request):
    if request.method == "POST":
        subject = data.get("subject")
        from_email = data.get("from")
        body = data.get("body")

        # Hier kannst du die Daten weiterverarbeiten oder speichern
        print("Spam gemeldet:")
        print("Betreff:", subject)
        print("Von:", from_email)
        print("Inhalt:", body)

        return JsonResponse({"status": "success", "message": "Spam gemeldet"})
    else:
        return JsonResponse({"status": "error", "message": "Ungültige Anfrage"})
