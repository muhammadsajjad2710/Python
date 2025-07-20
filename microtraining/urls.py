from django.urls import path
from .views import MicroTrainingCategoryListView, MicroTrainingListView


urlpatterns = [
    path(
        "microtrainings/",
        MicroTrainingCategoryListView.as_view(template_name="microtraining_category.html"),
        name="microtraining_category_list",
    ),
    path(
        "microtrainings/<int:pk>/",
        MicroTrainingListView.as_view(template_name="microtraining_list.html"),
        name="microtraining_list",
    ),
    path(
        "microtrainings/package/",
        MicroTrainingCategoryListView.as_view(template_name="microtraining_package.html"),
        name="microtraining_packages",
    ),
]
