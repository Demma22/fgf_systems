from django.urls import path
from .views import (
    RegistrationView,
    VerifyUserEmail,
    LoginUserView,
    LogoutUserView,
    TestAuthenticationView,
    PasswordResetRequestView,
    PasswordResetConfirm,
    SetNewPassword,
)
from urllib.parse import quote

urlpatterns = [
    path("api/v1/auth/register/", RegistrationView.as_view(), name="register"),
    path("api/v1/auth/verify-email/", VerifyUserEmail.as_view(), name="verify-email"),
    path("api/v1/auth/login/", LoginUserView.as_view(), name="login"),
    path("api/v1/auth/profile/", TestAuthenticationView.as_view(), name="test-auth"),
    path(
        "api/v1/auth/password-reset-request/",
        PasswordResetRequestView.as_view(),
        name="password-reset-request",
    ),
    path(
        f"api/v1/auth/password-reset-confirm/<str:uidb64>/<str:token>/",
        PasswordResetConfirm.as_view(),
        name="password-reset-confirm",
    ),
    path(
        "api/v1/auth/set-new-password/",
        SetNewPassword.as_view(),
        name="set-new-password",
    ),
    path(
        "api/v1/auth/logout/",
        LogoutUserView.as_view(),
        name="logout",
    ),
]
