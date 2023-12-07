from django.urls import path
from .views import (
    ClanListView,
    CulturalKingdomListView,
    EthnicityListView,
    EthnicGroupListView,
    CulturalIdentityListView,
)

urlpatterns = [
    path("api/clans/", ClanListView.as_view(), name="clan-list"),
    path(
        "api/cultural-kingdoms/",
        CulturalKingdomListView.as_view(),
        name="cultural-kingdom-list",
    ),
    path("api/ethnicities/", EthnicityListView.as_view(), name="ethnicity-list"),
    path("apiethnic-groups/", EthnicGroupListView.as_view(), name="ethnic-group-list"),
    path(
        "api/cultural-identities/",
        CulturalIdentityListView.as_view(),
        name="cultural-identity-list",
    ),
]
