from django.urls import path
from .views import (
    CountMedicinalPlantEntriesAPIView,
    CountPlantEntriesAPIView,
    PlantViewSet,
    PlantNameViewSet,
    MedicinalPlantViewSet,
    MedicinalPlantNameViewSet,
)

urlpatterns = [
    path(
        "api/total-plant-entries/",
        CountPlantEntriesAPIView.as_view(),
        name="total-plant-count",
    ),
    path(
        "api/total-medicinal-plant-entries/",
        CountMedicinalPlantEntriesAPIView.as_view(),
        name="total-medicinal-plant-entries",
    ),
    path(
        "api/plants/",
        PlantViewSet.as_view({"get": "list", "post": "create"}),
        name="plant_list_create",
    ),
    path(
        "api/plants/<int:pk>/",
        PlantViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="plant_detail",
    ),
    path(
        "api/plantnames/",
        PlantNameViewSet.as_view({"get": "list", "post": "create"}),
        name="plant_name_list_create",
    ),
    path(
        "api/plantnames/<int:pk>/",
        PlantNameViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="plant_name_detail",
    ),
    path(
        "api/medicinalplants/",
        MedicinalPlantViewSet.as_view({"get": "list", "post": "create"}),
        name="medicinal_plant_list_create",
    ),
    path(
        "api/medicinalplants/<int:pk>/",
        MedicinalPlantViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="medicinal_plant_detail",
    ),
    path(
        "api/medicinalplantnames/",
        MedicinalPlantNameViewSet.as_view({"get": "list", "post": "create"}),
        name="medicinal_plant_name_list_create",
    ),
    path(
        "api/medicinalplantnames/<int:pk>/",
        MedicinalPlantNameViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="medicinal_plant_name_detail",
    ),
    # Additional paths for review, approve, and reject actions
    path(
        "api/plants/<int:pk>/review-edit/",
        PlantViewSet.as_view({"patch": "review_edit_data"}),
        name="plant-review-edit",
    ),
    path(
        "api/plants/<int:pk>/approve/",
        PlantViewSet.as_view({"patch": "approve_data"}),
        name="plant-approve",
    ),
    path(
        "api/plants/<int:pk>/reject/",
        PlantViewSet.as_view({"delete": "reject_data"}),
        name="plant-reject",
    ),
    path(
        "api/medicinalplants/<int:pk>/review-edit/",
        MedicinalPlantViewSet.as_view({"patch": "review_edit_data"}),
        name="medicinal-plant-review-edit",
    ),
    path(
        "api/medicinalplants/<int:pk>/approve/",
        MedicinalPlantViewSet.as_view({"patch": "approve_data"}),
        name="medicinal-plant-approve",
    ),
    path(
        "api/medicinalplants/<int:pk>/reject/",
        MedicinalPlantViewSet.as_view({"delete": "reject_data"}),
        name="medicinal-plant-reject",
    ),
]
