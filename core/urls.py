from django.urls import path, include
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "FGF SYSTEMS"
admin.site.site_title = "Welcome to FGF systems "
admin.site.index_title = "Admin Dashboard"

schema_view = get_schema_view(
    openapi.Info(
        title="FUTURE GENERATIONS FOUNDATION REPOSITORY",
        default_version="v1",
        description="FUTURE GENERATIONS FOUNDATION BIO DIVERSITY PLATFORM ",
        terms_of_service="https://www.fgf.com/terms/",
        contact=openapi.Contact(email="info@fgf.com"),
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
    path("api/v1/animals/", include("animals.urls")),
    path("api/v1/cultures/", include("cultures.urls")),
    path("api/v1/plants/", include("plants.urls")),
    path("api/auth/v1/", include("accounts.urls")),
]

# Add the following lines for serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
