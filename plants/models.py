from django.db import models
from accounts.models import User
from django.forms import ValidationError


# Choices for life_form field
LIFE_FORM_CHOICES = [
    ("forest", "Forest"),
    ("meadow", "Meadow"),
    ("climber", "Climber"),
    ("grassland", "Grassland"),
    ("herb", "Herb"),
    ("shrub", "Shrub"),
    ("tree", "Tree"),
]


class Language(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Plant(models.Model):
    botanical_name = models.CharField(
        max_length=100, unique=True, blank=True, null=True
    )
    region_in_Uganda = models.CharField(max_length=100, blank=True, null=True)
    unique_habitat = models.CharField(max_length=100, blank=True, null=True)
    life_form = models.CharField(max_length=100, choices=LIFE_FORM_CHOICES, null=True)
    climate_Impact = models.CharField(max_length=100, blank=True, null=True)
    threats = models.CharField(max_length=100, blank=True, null=True)
    known_values = models.TextField()
    image = models.ImageField(upload_to="plant_images/", blank=True, null=True)
    video = models.FileField(upload_to="plant_videos/", blank=True, null=True)
    audio = models.FileField(upload_to="plant_audio/", blank=True, null=True)
    notes = models.TextField()
    citation = models.CharField(max_length=255)
    names = models.ManyToManyField(
        Language, through="PlantName", related_name="plant_names"
    )

    def __str__(self):
        return f"Plant: {self.botanical_name}"


class PlantName(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Check for duplicate names within the same language for a plant
        if PlantName.objects.filter(
            plant=self.plant, language=self.language, name=self.name
        ).exists():
            raise ValidationError(
                "Plant name in the specified language must be unique for each plant."
            )

        # Check for duplicate names in other languages for a plant
        if (
            PlantName.objects.filter(plant=self.plant, name=self.name)
            .exclude(language=self.language)
            .exists()
        ):
            raise ValidationError(
                "Plant name must be unique across all languages for each plant."
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Plant Name: {self.name} - Language: {self.language}"


class MedicinalPlant(models.Model):
    plant = models.OneToOneField(
        Plant, on_delete=models.CASCADE, related_name="medicinal_info"
    )
    health_issues = models.TextField()
    part_used = models.CharField(max_length=100, blank=True, null=True)
    preparation_steps = models.TextField()
    dosage = models.CharField(max_length=100, blank=True, null=True)
    contraindications = models.TextField()
    shelf_life = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField()
    cultural_value = models.TextField()
    contributor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    names = models.ManyToManyField(
        Language, through="MedicinalPlantName", related_name="medicinal_plant_names"
    )

    def __str__(self):
        return f"Medicinal Info for Plant: {self.plant.botanical_name}"


class MedicinalPlantName(models.Model):
    medicinal_plant = models.ForeignKey(MedicinalPlant, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Check for duplicate names within the same language for a medicinal plant
        if MedicinalPlantName.objects.filter(
            medicinal_plant=self.medicinal_plant, language=self.language, name=self.name
        ).exists():
            raise ValidationError(
                "Medicinal plant name in the specified language must be unique for each medicinal plant."
            )

        # Check for duplicate names in other languages for a medicinal plant
        if (
            MedicinalPlantName.objects.filter(
                medicinal_plant=self.medicinal_plant, name=self.name
            )
            .exclude(language=self.language)
            .exists()
        ):
            raise ValidationError(
                "Medicinal plant name must be unique across all languages for each medicinal plant."
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Medicinal Plant Name: {self.name} - Language: {self.language}"
