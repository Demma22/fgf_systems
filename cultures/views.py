from django.db import models
from rest_framework import generics, filters
from .models import Clan, CulturalKingdom, Ethnicity, EthnicGroup, CulturalIdentity
from .serializers import (
    ClanSerializer,
    CulturalKingdomSerializer,
    EthnicitySerializer,
    EthnicGroupSerializer,
    CulturalIdentitySerializer,
)


class ClanListView(generics.ListCreateAPIView):
    queryset = Clan.objects.all()
    serializer_class = ClanSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["clan_name", "clan_seat"]


class CulturalKingdomListView(generics.ListCreateAPIView):
    queryset = CulturalKingdom.objects.all()
    serializer_class = CulturalKingdomSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["kingdom_name", "title_of_leader"]


class EthnicityListView(generics.ListCreateAPIView):
    queryset = Ethnicity.objects.all()
    serializer_class = EthnicitySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["ethnicity_name", "region_in_Uganda"]


class EthnicGroupListView(generics.ListCreateAPIView):
    queryset = EthnicGroup.objects.all()
    serializer_class = EthnicGroupSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["ethnic_group_name", "region_in_Uganda"]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.annotate(total_entries=models.Count("culturalidentity"))


class CulturalIdentityListView(generics.ListCreateAPIView):
    queryset = CulturalIdentity.objects.all()
    serializer_class = CulturalIdentitySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["ethnic_group__ethnic_group_name"]
