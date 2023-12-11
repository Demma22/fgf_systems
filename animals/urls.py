from django.urls import path
from .views import (
    TotalAnimalCountAPIView,
    TotalClassificationCountAPIView,
    TotalSpeciesCountAPIView,
    AnimalListCreateView,
    AnimalDetailView,
    AnimalClassificationListCreateView,
    AnimalClassificationDetailView,
    AnimalLocalNameListCreateView,
    AnimalLocalNameDetailView,
    submit_animal_data,
    review_edit_animal_data,
    approve_animal_data,
    reject_animal_data,
)

urlpatterns = [
    path(
        "api/total-animal-count/",
        TotalAnimalCountAPIView.as_view(),
        name="total-animal-count",
    ),
    path(
        "api/total-classification-count/",
        TotalClassificationCountAPIView.as_view(),
        name="total-classification-count",
    ),
    path(
        "api/total-species-count/",
        TotalSpeciesCountAPIView.as_view(),
        name="total-species-count",
    ),
    path("api/animals/", AnimalListCreateView.as_view(), name="animal-list-create"),
    path("api/animals/<int:pk>/", AnimalDetailView.as_view(), name="animal-detail"),
    path(
        "api/classifications/",
        AnimalClassificationListCreateView.as_view(),
        name="classification-list-create",
    ),
    path(
        "api/classifications/<int:pk>/",
        AnimalClassificationDetailView.as_view(),
        name="classification-detail",
    ),
    path(
        "api/local-names/",
        AnimalLocalNameListCreateView.as_view(),
        name="local-name-list-create",
    ),
    path(
        "api/local-names/<int:pk>/",
        AnimalLocalNameDetailView.as_view(),
        name="local-name-detail",
    ),
    path("api/submit-animal-data/", submit_animal_data, name="submit-animal-data"),
    path(
        "api/review-edit-animal-data/<int:animal_id>/",
        review_edit_animal_data,
        name="review-edit-animal-data",
    ),
    path(
        "api/approve-animal-data/<int:animal_id>/",
        approve_animal_data,
        name="approve-animal-data",
    ),
    path(
        "api/reject-animal-data/<int:animal_id>/",
        reject_animal_data,
        name="reject-animal-data",
    ),
]
