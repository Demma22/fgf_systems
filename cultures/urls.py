from django.urls import path
from .views import (
    ClanListView,
    CulturalKingdomListView,
    EthnicityListView,
    EthnicGroupListView,
    CulturalIdentityListView,
)

urlpatterns = [
    path("clans/", ClanListView.as_view(), name="clan-list"),
    path(
        "total-clan-entries/",
        ClanListView.as_view(),
        name="total-clan-entries",
    ),
    path(
        "cultural-kingdoms/",
        CulturalKingdomListView.as_view(),
        name="cultural-kingdom-list",
    ),
    path(
        "total-cultural-kingdom-entries/",
        CulturalKingdomListView.as_view(),
        name="total-cultural-kingdom-entries",
    ),
    path("ethnicity/", EthnicityListView.as_view(), name="ethnicity-list"),
    path(
        "total-entries-ethnicity/",
        EthnicityListView.as_view(),
        name="total-ethnicity-entries",
    ),
    path(
        "ethnic-groups/",
        EthnicGroupListView.as_view(),
        name="ethnic-group-list",
    ),
    path(
        "total-entries-ethnic-groups/",
        EthnicGroupListView.as_view(),
        name="total-ethnic-group-entries",
    ),
    path(
        "cultural-identities/",
        CulturalIdentityListView.as_view(),
        name="cultural-identity-list",
    ),
    path(
        "total-entries-cultural-identity/",
        CulturalIdentityListView.as_view(),
        name="total-entries-cultural-identity",
    ),
    path(
        "cultural-identities/<int:cultural_identity_id>/review-edit/",
        CulturalIdentityListView.review_edit_data,
        name="cultural-identity-review-edit",
    ),
    path(
        "cultural-identities/<int:cultural_identity_id>/approve/",
        CulturalIdentityListView.approve_data,
        name="cultural-identity-approve",
    ),
    path(
        "cultural-identities/<int:cultural_identity_id>/reject/",
        CulturalIdentityListView.reject_data,
        name="cultural-identity-reject",
    ),
]
