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
        "register/contributor/",
        ContributorRegistrationView.as_view(),
        name="contributor-register",
    ),
    path("register/admin/", AdminRegistrationView.as_view(), name="admin-register"),
    path(
        "login/contributor/", ContributorLoginView.as_view(), name="contributor-login"
    ),
    path("login/admin/", AdminLoginView.as_view(), name="admin-login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("password-reset/", PasswordResetRequestView.as_view(), name="password-reset"),
    path(
        "password-reset/confirm/",
        SetNewPasswordView.as_view(),
        name="password-reset-confirm",
    ),
]
