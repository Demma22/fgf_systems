from rest_framework import viewsets, generics, filters, permissions
from rest_framework.response import Response
from .models import Plant, PlantName, MedicinalPlant, MedicinalPlantName
from .serializers import (
    PlantSerializer,
    PlantNameSerializer,
    MedicinalPlantSerializer,
    MedicinalPlantNameSerializer,
)


class CountEntriesAPIView(generics.GenericAPIView):
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


class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["botanical_name", "region_in_Uganda"]
    ordering_fields = "__all__"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        count = queryset.count()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"count": count, "plants": serializer.data})


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

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        count = queryset.count()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"count": count, "medicinal_plants": serializer.data})


class MedicinalPlantNameViewSet(viewsets.ModelViewSet):
    queryset = MedicinalPlantName.objects.all()
    serializer_class = MedicinalPlantNameSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "language__name"]
    ordering_fields = "__all__"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
