from rest_framework import viewsets, generics, filters, permissions
from rest_framework.response import Response
from .models import Plant, PlantName, MedicinalPlant, MedicinalPlantName
from .serializers import (
    CountEntriesSerializer,
    PlantSerializer,
    PlantNameSerializer,
    MedicinalPlantSerializer,
    MedicinalPlantNameSerializer,
)
from rest_framework.decorators import action


class CountPlantEntriesAPIView(generics.GenericAPIView):
    serializer_class = CountEntriesSerializer  # Add this line

    def get(self, request, *args, **kwargs):
        plant_count = Plant.objects.count()
        medicinal_plant_count = MedicinalPlant.objects.count()

        # Use the serializer to structure the response
        serializer = self.get_serializer(
            {
                "plant_entries_count": plant_count,
                "medicinal_plant_entries_count": medicinal_plant_count,
            }
        )


class CountPlantEntriesAPIView(generics.GenericAPIView):
    """
    View to count all plant and medicinal plant entries.
    """

    def get(self, request, *args, **kwargs):
        plant_count = Plant.objects.count()
        medicinal_plant_count = MedicinalPlant.objects.count()

        return Response(
            {
                "plant_entries_count": plant_count,
                "medicinal_plant_entries_count": medicinal_plant_count,
            }
        )


class CountMedicinalPlantEntriesAPIView(generics.GenericAPIView):
    """
    View to count all medicinal plant entries.
    """

    def get(self, request, *args, **kwargs):
        medicinal_plant_count = MedicinalPlant.objects.count()

        return Response(
            {
                "medicinal_plant_entries_count": medicinal_plant_count,
            }
        )


class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["botanical_name", "region_in_Uganda"]
    ordering_fields = "__all__"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=["post"])
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        count = queryset.count()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"count": count, "plants": serializer.data})

    @action(detail=True, methods=["post"])
    def review_edit_data(self, request, pk=None):
        plant_instance = self.get_object()
        serializer = PlantSerializer(plant_instance)
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def approve_data(self, request, pk=None):
        plant_instance = self.get_object()
        plant_instance.is_approved = True  # Assuming you have an 'is_approved' field
        plant_instance.save()
        return Response({"message": "Plant data approved successfully."})

    @action(detail=True, methods=["post"])
    def reject_data(self, request, pk=None):
        plant_instance = self.get_object()
        plant_instance.delete()
        return Response({"message": "Plant data rejected successfully."})


class PlantNameViewSet(viewsets.ModelViewSet):
    queryset = PlantName.objects.all()
    serializer_class = PlantNameSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "language__name"]
    ordering_fields = "__all__"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MedicinalPlantViewSet(viewsets.ModelViewSet):
    queryset = MedicinalPlant.objects.all()
    serializer_class = MedicinalPlantSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["plant__botanical_name", "health_issues"]
    ordering_fields = "__all__"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=["post"])
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        count = queryset.count()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"count": count, "medicinal_plants": serializer.data})

    @action(detail=True, methods=["post"])
    def review_edit_data(self, request, pk=None):
        medicinal_plant_instance = self.get_object()
        serializer = MedicinalPlantSerializer(medicinal_plant_instance)
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def approve_data(self, request, pk=None):
        medicinal_plant_instance = self.get_object()
        medicinal_plant_instance.is_approved = (
            True  # Assuming you have an 'is_approved' field
        )
        medicinal_plant_instance.save()
        return Response({"message": "Medicinal plant data approved successfully."})

    @action(detail=True, methods=["post"])
    def reject_data(self, request, pk=None):
        medicinal_plant_instance = self.get_object()
        medicinal_plant_instance.delete()
        return Response({"message": "Medicinal plant data rejected successfully."})


class MedicinalPlantNameViewSet(viewsets.ModelViewSet):
    queryset = MedicinalPlantName.objects.all()
    serializer_class = MedicinalPlantNameSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "language__name"]
    ordering_fields = "__all__"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
