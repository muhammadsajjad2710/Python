from django.views.generic import TemplateView
from web_project import TemplateLayout
from web_project.template_helpers.theme import TemplateHelper
from apps.phishing.models import PhishingTemplate, Indicator, Gif, Language
from apps.microtraining.models import MicroTraining, MicroTrainingTranslation
from django.utils.translation import get_language
from django.shortcuts import get_object_or_404
import random
import requests

"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to front_pages/urls.py file for more pages.
"""
GIPHY_API_KEY = 'QWKLmYST1eORLxFMOOvbkopoCmXPGF2W'

class FrontPagesView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        # Update the context
        context.update(
            {
                "layout": "front",
                "layout_path": TemplateHelper.set_layout("layout_front.html", context),
                "active_url": self.request.path,  # Get the current url path (active URL) from request
            }
        )

        # map_context according to updated context values
        TemplateHelper.map_context(context)

        return context

class SimulationSuccessView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        # get a random gif
        gif_url = self.get_random_gif_url('success')

        # get simulation
        campaign_id = kwargs['pk']
        phishing_template = get_object_or_404(PhishingTemplate, pk=campaign_id)
        relevant_indicators = phishing_template.indicators_of_compromise.all()

        phishing_email = {
            "subject": phishing_template.sending_subject,
            "content": phishing_template.content,
            "sender_name": phishing_template.sending_name,
            "sender_email": phishing_template.sending_email,
        }

        # Update the context
        context.update(
            {
                "layout": "front",
                "layout_path": TemplateHelper.set_layout("layout_front.html", context),
                "active_url": self.request.path,  # Get the current url path (active URL) from request
                "gif_url": gif_url,  # Random GIF
                "phishing_email": phishing_email,  # Phishing-Mail für das Mikrotraining
                "indicators": relevant_indicators,

            }
        )

        # map_context according to updated context values
        TemplateHelper.map_context(context)

        return context

    def get_random_gif_url(self, gif_type):
        # Holen aller GIF-IDs für den angegebenen Typ aus der Datenbank
        gif_entries = Gif.objects.filter(gif_type=gif_type)

        if not gif_entries:
            return None  # oder ein Standard-GIF-URL zurückgeben

        # Wählen eines zufälligen GIFs
        gif_entry = random.choice(gif_entries)
        gif_id = gif_entry.gif_id

        # URL zur Giphy API zum Abrufen des GIFs anhand der ID
        giphy_url = f"https://api.giphy.com/v1/gifs/{gif_id}?api_key={GIPHY_API_KEY}"

        # HTTP GET Anfrage an die Giphy API
        response = requests.get(giphy_url)
        data = response.json()

        # Überprüfen der Struktur der JSON-Antwort
        if 'data' in data and 'images' in data['data'] and 'original' in data['data']['images'] and 'url' in data['data']['images']['original']:
            gif_url = data['data']['images']['original']['url']
        else:
            gif_url = None  # oder ein Standard-GIF-URL zurückgeben

        return gif_url


class MicrotrainingView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        # get a random gif
        gif_url = self.get_random_gif_url('success')

        # get simulation
        phishing_template = PhishingTemplate.objects.first()
        relevant_indicators = phishing_template.indicators_of_compromise.all()

        current_language = get_language()

        # Versuche, die aktuelle Sprache zu bekommen, ansonsten nimm 'en'
        try:
            language = Language.objects.get(code=current_language)
        except Language.DoesNotExist:
            language = Language.objects.get(code='en')

        # Hole die Übersetzungen basierend auf der gefundenen Sprache
        microtraining = MicroTrainingTranslation.objects.filter(language=language).first()

        # Wenn keine Übersetzungen für die gefundene Sprache vorhanden sind, nimm die englischen Übersetzungen
        if not microtraining:
            language = Language.objects.get(code='en')
            microtraining = MicroTrainingTranslation.objects.filter(language=language).first()

        phishing_email = {
            "subject": "Important Update Required",
            "body": "Dear user, please update your account information by clicking the link below.",
            "sender": "no-reply@fakeemail.com"
        }

        # Update the context
        context.update(
            {
                "layout": "front",
                "layout_path": TemplateHelper.set_layout("layout_front.html", context),
                "active_url": self.request.path,  # Get the current url path (active URL) from request
                "gif_url": gif_url,  # Random GIF
                "phishing_email": phishing_email,  # Phishing-Mail für das Mikrotraining
                "indicators": relevant_indicators,
                "microtraining": microtraining,

            }
        )

        # map_context according to updated context values
        TemplateHelper.map_context(context)

        return context

    def get_random_gif_url(self, gif_type):
        # Holen aller GIF-IDs für den angegebenen Typ aus der Datenbank
        gif_entries = Gif.objects.filter(gif_type=gif_type)

        if not gif_entries:
            return None  # oder ein Standard-GIF-URL zurückgeben

        # Wählen eines zufälligen GIFs
        gif_entry = random.choice(gif_entries)
        gif_id = gif_entry.gif_id

        # URL zur Giphy API zum Abrufen des GIFs anhand der ID
        giphy_url = f"https://api.giphy.com/v1/gifs/{gif_id}?api_key={GIPHY_API_KEY}"

        # HTTP GET Anfrage an die Giphy API
        response = requests.get(giphy_url)
        data = response.json()

        # Überprüfen der Struktur der JSON-Antwort
        if 'data' in data and 'images' in data['data'] and 'original' in data['data']['images'] and 'url' in data['data']['images']['original']:
            gif_url = data['data']['images']['original']['url']
        else:
            gif_url = None  # oder ein Standard-GIF-URL zurückgeben

        return gif_url
