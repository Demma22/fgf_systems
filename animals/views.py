# views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Animal, AnimalClassification, AnimalLocalName
from .serializers import (
    AnimalSerializer,
    AnimalClassificationSerializer,
    AnimalLocalNameSerializer,
    CountEntriesSerializer,
)


class CountEntriesAPIView(generics.ListAPIView):
    serializer_class = CountEntriesSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to view the counts

    def get_queryset(self):
        # Count the total number of entries for animals
        total_animal_count = Animal.objects.count()

        # Count the total number of entries for animal classifications
        total_classification_count = AnimalClassification.objects.count()

        # Count the total number of animal species
        total_species_count = AnimalClassification.objects.aggregate(
            total_species_count=Count("species", distinct=True)
        )["total_species_count"]

        return [
            {
                "total_animal_count": total_animal_count,
                "total_classification_count": total_classification_count,
                "total_species_count": total_species_count,
            }
        ]


class AnimalListCreateView(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AnimalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    filter_backends = [DjangoFilterBackend]
    serializer_class = AnimalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AnimalClassificationListCreateView(generics.ListCreateAPIView):
    queryset = AnimalClassification.objects.all()
    serializer_class = AnimalClassificationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AnimalClassificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnimalClassification.objects.all()
    filter_backends = [DjangoFilterBackend]
    serializer_class = AnimalClassificationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AnimalLocalNameListCreateView(generics.ListCreateAPIView):
    queryset = AnimalLocalName.objects.all()
    serializer_class = AnimalLocalNameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AnimalLocalNameDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnimalLocalName.objects.all()
    filter_backends = [DjangoFilterBackend]
    serializer_class = AnimalLocalNameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def submit_animal_data(request):
    data = request.data
    data[
        "contributor_name"
    ] = request.user  # Set the contributor_name to the current user instance

    serializer = AnimalSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PATCH"])
@permission_classes([permissions.IsAdminUser])
def approve_animal_data(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    animal.is_approved = True
    animal.save()
    return Response({"message": "Animal data approved successfully."})


@api_view(["PATCH"])
@permission_classes([permissions.IsAdminUser])
def reject_animal_data(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    animal.delete()
    return Response({"message": "Animal data rejected successfully."})
