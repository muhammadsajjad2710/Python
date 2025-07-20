from django.views.generic import TemplateView
from web_project import TemplateLayout
from .models import MicroTrainingCategory, MicroTraining
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from apps.settingsmanager.models import MicrotrainingCategoryActivation, MicrotrainingTrainingActivation

"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to sample/urls.py file for more pages.
"""
class MicroTrainingCategoryListView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        categories = MicroTrainingCategory.objects.all()
        category_activations = {ca.category_id: ca.is_active for ca in MicrotrainingCategoryActivation.objects.all()}

        categories_with_activation = []
        for category in categories:
            is_active = category_activations.get(category.id, category.default_active)
            categories_with_activation.append((category, is_active))

        context.update({
            'categories_with_activation': categories_with_activation,
        })
        return context

    def post(self, request, *args, **kwargs):
        category_id = request.POST.get('category_id')
        is_active = request.POST.get('is_active') == 'true'

        if category_id:
            category = get_object_or_404(MicroTrainingCategory, id=category_id)
            MicrotrainingCategoryActivation.objects.update_or_create(
                category=category,
                defaults={'is_active': is_active}
            )

        return JsonResponse({'status': 'success'})

class MicroTrainingListView(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        category_id = kwargs.get('pk')
        category = get_object_or_404(MicroTrainingCategory, pk=category_id)
        trainings = category.microtraining_set.all()  # Stelle sicher, dass das Related Name korrekt ist
        training_activations = {ta.training_id: ta.is_active for ta in MicrotrainingTrainingActivation.objects.filter(training__in=trainings)}

        trainings_with_activation = []
        for training in trainings:
            is_active = training_activations.get(training.id, training.default_active)
            trainings_with_activation.append((training, is_active))

        context.update({
            'category': category,
            'trainings_with_activation': trainings_with_activation,
        })
        return context

    def post(self, request, *args, **kwargs):
        training_id = request.POST.get('training_id')
        is_active = request.POST.get('is_active') == 'true'

        if training_id:
            training = get_object_or_404(MicroTraining, id=training_id)
            MicrotrainingTrainingActivation.objects.update_or_create(
                training=training,
                defaults={'is_active': is_active}
            )

        return JsonResponse({'status': 'success'})
