from django.urls import path
from .views import UsersView, UsersAccountView, UsersData, phishing_simulations_data
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path(
        "users/edit",
        login_required(UsersView.as_view(template_name="users_edit.html")),
        name="users-edit",
    ),
	path(
        "users/overview",
        login_required(UsersView.as_view(template_name="users_overview.html")),
        name="users-overview",
    ),
	path(
        "users/add",
        login_required(UsersView.as_view(template_name="users_add.html")),
        name="users-import",
    ),
	path(
        "users/import",
        login_required(UsersView.as_view(template_name="users_import.html")),
        name="users-import",
    ),
    path(
        "users/account/<int:pk>/",
        login_required(UsersAccountView.as_view(template_name="users_view_account.html")),
        name="users-account",
    ),
    path(
        "api/phishing-simulations-data/<int:user_id>/",
        phishing_simulations_data,
        name='phishing_simulations_data'
    ),
    path(
        "api/users-data/",
        UsersData,
        name='users_data'
    ),
]
