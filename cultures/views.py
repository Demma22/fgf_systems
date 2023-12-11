from django.db.models import Count
from rest_framework import generics, filters, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Clan, CulturalKingdom, Ethnicity, EthnicGroup, CulturalIdentity
from .serializers import (
    ClanSerializer,
    CulturalKingdomSerializer,
    EthnicitySerializer,
    EthnicGroupSerializer,
    CulturalIdentitySerializer,
)


class TotalEntriesMixin:
    def get_total_entries(self, queryset):
        return queryset.count()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        total_entries = self.get_total_entries(queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response({"total_entries": total_entries, "entries": serializer.data})


class ClanListView(TotalEntriesMixin, generics.ListCreateAPIView):
    queryset = Clan.objects.all()
    serializer_class = ClanSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["clan_name", "clan_seat"]

    def get_total_entries(self, queryset):
        return Clan.objects.count()


class CulturalKingdomListView(TotalEntriesMixin, generics.ListCreateAPIView):
    queryset = CulturalKingdom.objects.all()
    serializer_class = CulturalKingdomSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["kingdom_name", "title_of_leader"]

    def get_total_entries(self, queryset):
        return CulturalKingdom.objects.count()


class EthnicityListView(TotalEntriesMixin, generics.ListCreateAPIView):
    queryset = Ethnicity.objects.all()
    serializer_class = EthnicitySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["ethnicity_name", "region_in_Uganda"]

    def get_total_entries(self, queryset):
        return Ethnicity.objects.count()


class EthnicGroupListView(TotalEntriesMixin, generics.ListCreateAPIView):
    queryset = EthnicGroup.objects.all()
    serializer_class = EthnicGroupSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["ethnic_group_name", "region_in_Uganda"]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.annotate(total_entries=Count("ethnicity__culturalidentity"))

    def get_total_entries(self, queryset):
        return queryset.aggregate(total_entries=Count("id"))["total_entries"]


class CulturalIdentityListView(TotalEntriesMixin, generics.ListCreateAPIView):
    queryset = CulturalIdentity.objects.all()
    serializer_class = CulturalIdentitySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["ethnic_group__ethnic_group_name"]

    def review_edit_data(self, request, cultural_identity_id):
        cultural_identity = get_object_or_404(CulturalIdentity, pk=cultural_identity_id)

        if request.method == "GET":
            serializer = CulturalIdentitySerializer(cultural_identity)
            return Response(serializer.data)

        elif request.method == "PATCH":
            serializer = CulturalIdentitySerializer(
                cultural_identity, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def approve_data(self, request, cultural_identity_id):
        cultural_identity = get_object_or_404(CulturalIdentity, pk=cultural_identity_id)
        cultural_identity.is_approved = True
        cultural_identity.save()
        return Response({"message": "Data approved successfully."})

    def reject_data(self, request, cultural_identity_id):
        cultural_identity = get_object_or_404(CulturalIdentity, pk=cultural_identity_id)
        cultural_identity.delete()
        return Response({"message": "Data rejected successfully."})
