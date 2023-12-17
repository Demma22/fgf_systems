# accounts/urls.py
from django.urls import path
from .views import (
    ContributorRegistrationView,
    AdminRegistrationView,
    ContributorLoginView,
    AdminLoginView,
    LogoutView,
    PasswordResetRequestView,
    SetNewPasswordView,
)

urlpatterns = [
    path(
        "api/v1/auth/register/contributor/",
        ContributorRegistrationView.as_view(),
        name="contributor-register",
    ),
    path(
        "api/v1/auth/register/admin/", AdminRegistrationView.as_view(), name="admin-register"
    ),
    path(
        "api/v1/auth/login/contributor/",
        ContributorLoginView.as_view(),
        name="contributor-login",
    ),
    path("api/v1/auth/login/admin/", AdminLoginView.as_view(), name="admin-login"),
    path("api/v1/logout/", LogoutView.as_view(), name="logout"),
    path(
        "api/v1/password-reset/",
        PasswordResetRequestView.as_view(),
        name="password-reset",
    ),
    path(
        "api/v1/auth/password-reset/confirm/",
        SetNewPasswordView.as_view(),
        name="password-reset-confirm",
    ),
]
