from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CountEntriesAPIView,
    PlantViewSet,
    PlantNameViewSet,
    MedicinalPlantViewSet,
    MedicinalPlantNameViewSet,
)


urlpatterns = [
    path(
        "api/count-plant-entries/", CountEntriesAPIView.as_view(), name="count_entries"
    ),
    # Use the .as_view() method with the specific actions for each ViewSet
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

]


