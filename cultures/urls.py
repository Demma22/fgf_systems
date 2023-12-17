from django.urls import path
from .views import (
    ClanListView,
    CulturalKingdomListView,
    EthnicityListView,
    EthnicGroupListView,
    CulturalIdentityListView,
)

urlpatterns = [
    path("api/v1/clans/", ClanListView.as_view(), name="clan-list"),
    path(
        "api/v1/total-clan-entries/",
        ClanListView.as_view(),
        name="total-clan-entries",
    ),
    path(
        "api/v1/cultural-kingdoms/",
        CulturalKingdomListView.as_view(),
        name="cultural-kingdom-list",
    ),
    path(
        "api/v1/total-cultural-kingdom-entries/",
        CulturalKingdomListView.as_view(),
        name="total-cultural-kingdom-entries",
    ),
    path("api/v1/cultures/", EthnicityListView.as_view(), name="ethnicity-list"),
    path(
        "api/v1/total-entries-cultures/",
        EthnicityListView.as_view(),
        name="total-ethnicity-entries",
    ),
    path(
        "api/v1/ethnic-groups/",
        EthnicGroupListView.as_view(),
        name="ethnic-group-list",
    ),
    path(
        "api/v1/total-entries-ethnic-groups/",
        EthnicGroupListView.as_view(),
        name="total-ethnic-group-entries",
    ),
    path(
        "api/v1/cultural-identities/",
        CulturalIdentityListView.as_view(),
        name="cultural-identity-list",
    ),
    path(
        "api/v1/total-entries-cultural-identity/",
        CulturalIdentityListView.as_view(),
        name="total-entries-cultural-identity",
    ),
    path(
        "api/v1/cultural-identities/<int:cultural_identity_id>/review-edit/",
        CulturalIdentityListView.review_edit_data,
        name="cultural-identity-review-edit",
    ),
    path(
        "api/v1/cultural-identities/<int:cultural_identity_id>/approve/",
        CulturalIdentityListView.approve_data,
        name="cultural-identity-approve",
    ),
    path(
        "api/v1/cultural-identities/<int:cultural_identity_id>/reject/",
        CulturalIdentityListView.reject_data,
        name="cultural-identity-reject",
    ),
]
