# urls.py
from django.urls import path, include
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



admin.site.site_header = "FGF SYSTEMS"
admin.site.site_title = "Welcome to FGF systems "
admin.site.index_title = "Admin Dashboard"


schema_view = get_schema_view(
    openapi.Info(
        title="FUTURE GENERATIONS FOUNDATION REPOSITORY",
        default_version="v1",
        description="Description of your API",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/schema/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "api/docs/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    path("", include("animals.urls"), name="animals"),
    path("", include("cultures.urls"), name="cultures"),
    path("", include("plants.urls"), name="plants"),
    path("", include("accounts.urls"), name="accounts"),
]
