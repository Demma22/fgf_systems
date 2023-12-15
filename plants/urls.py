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
        "total-plant-entries/",
        CountPlantEntriesAPIView.as_view(),
        name="total-plant-count",
    ),
    path(
        "total-medicinal-plant-entries/",
        CountMedicinalPlantEntriesAPIView.as_view(),
        name="total-medicinal-plant-entries",
    ),
    path(
        "plants/",
        PlantViewSet.as_view({"get": "list", "post": "create"}),
        name="plant_list_create",
    ),
    path(
        "plants/<int:pk>/",
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
        "plantnames/",
        PlantNameViewSet.as_view({"get": "list", "post": "create"}),
        name="plant_name_list_create",
    ),
    path(
        "plantnames/<int:pk>/",
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
        "medicinalplants/",
        MedicinalPlantViewSet.as_view({"get": "list", "post": "create"}),
        name="medicinal_plant_list_create",
    ),
    path(
        "medicinalplants/<int:pk>/",
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
        "medicinalplantnames/",
        MedicinalPlantNameViewSet.as_view({"get": "list", "post": "create"}),
        name="medicinal_plant_name_list_create",
    ),
    path(
        "medicinalplantnames/<int:pk>/",
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
        "plants/<int:pk>/review-edit/",
        PlantViewSet.as_view({"patch": "review_edit_data"}),
        name="plant-review-edit",
    ),
    path(
        "plants/<int:pk>/approve/",
        PlantViewSet.as_view({"patch": "approve_data"}),
        name="plant-approve",
    ),
    path(
        "plants/<int:pk>/reject/",
        PlantViewSet.as_view({"delete": "reject_data"}),
        name="plant-reject",
    ),
    path(
        "medicinalplants/<int:pk>/review-edit/",
        MedicinalPlantViewSet.as_view({"patch": "review_edit_data"}),
        name="medicinal-plant-review-edit",
    ),
    path(
        "medicinalplants/<int:pk>/approve/",
        MedicinalPlantViewSet.as_view({"patch": "approve_data"}),
        name="medicinal-plant-approve",
    ),
    path(
        "medicinalplants/<int:pk>/reject/",
        MedicinalPlantViewSet.as_view({"delete": "reject_data"}),
        name="medicinal-plant-reject",
    ),
]
