from django.urls import path
from .views import (
    CountEntriesAPIView,
    AnimalListCreateView,
    AnimalDetailView,
    AnimalClassificationListCreateView,
    AnimalClassificationDetailView,
    AnimalLocalNameListCreateView,
    AnimalLocalNameDetailView,
    submit_animal_data,
    approve_animal_data,
    reject_animal_data,
)

urlpatterns = [
    path("api/count-animal-entries/", CountEntriesAPIView.as_view(), name="count-animal-entries"),
    path("api/animals/", AnimalListCreateView.as_view(), name="animal-list-create"),
    path("api/animals/<int:pk>/", AnimalDetailView.as_view(), name="animal-detail"),
    path(
        "api/animal-classifications/",
        AnimalClassificationListCreateView.as_view(),
        name="animal-classification-list-create",
    ),
    path(
        "api/animal-classifications/<int:pk>/",
        AnimalClassificationDetailView.as_view(),
        name="animal-classification-detail",
    ),
    path(
        "api/animal-local-names/",
        AnimalLocalNameListCreateView.as_view(),
        name="animal-local-name-list-create",
    ),
    path(
        "api/animal-local-names/<int:pk>/",
        AnimalLocalNameDetailView.as_view(),
        name="animal-local-name-detail",
    ),
    path("api/submit-animal/", submit_animal_data, name="submit_animal_data"),
    path("api/approve-animal/<int:animal_id>/", approve_animal_data, name="approve_animal_data"),
    path("api/reject-animal/<int:animal_id>/", reject_animal_data, name="reject_animal_data"),
]
