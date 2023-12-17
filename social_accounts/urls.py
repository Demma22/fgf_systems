from django.urls import path
from .views import GoogleSignInView

urlpatterns = [
    path("api/v1/google/", GoogleSignInView.as_view(), name="google"),
]
