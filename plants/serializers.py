from rest_framework import serializers
from .models import Plant, PlantName, MedicinalPlant, MedicinalPlantName


class PlantNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantName
        fields = "__all__"


class MedicinalPlantNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicinalPlantName
        fields = "__all__"


class PlantSerializer(serializers.ModelSerializer):
    names = PlantNameSerializer(many=True, read_only=True)

    class Meta:
        model = Plant
        fields = "__all__"


class MedicinalPlantSerializer(serializers.ModelSerializer):
    medicinal_names = MedicinalPlantNameSerializer(many=True, read_only=True)

    class Meta:
        model = MedicinalPlant
        fields = "__all__"
