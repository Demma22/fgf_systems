# serializers.py
from rest_framework import serializers
from .models import Animal, AnimalClassification, AnimalLocalName


class CountEntriesSerializer(serializers.Serializer):
    total_animal_count = serializers.IntegerField()
    total_classification_count = serializers.IntegerField()
    total_species_count = serializers.IntegerField()


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = "__all__"


class AnimalClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalClassification
        fields = "__all__"


class AnimalLocalNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalLocalName
        fields = "__all__"
