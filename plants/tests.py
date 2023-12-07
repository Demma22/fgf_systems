# plants/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Language, Plant, PlantName, MedicinalPlant, MedicinalPlantName


class PlantModelTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create a language for testing
        self.language = Language.objects.create(name="English")

        # Create a plant for testing
        self.plant = Plant.objects.create(
            botanical_name="Test Plant",
            region_in_Uganda="Test Region",
            habitat="Test Habitat",
            life_form="tree",
            social_value="Test Social Value",
            economical_value="Test Economical Value",
            cultural_value="Test Cultural Value",
            other_value="Test Other Value",
            notes="Test Notes",
            contributor=self.user,
            citation="Test Citation",
        )

        # Create a plant name for testing
        self.plant_name = PlantName.objects.create(
            plant=self.plant,
            language=self.language,
            language_name="Test Language Name",
            plant_name="Test Plant Name",
            is_english=True,
        )

        # Create a medicinal plant for testing
        self.medicinal_plant = MedicinalPlant.objects.create(
            plant=self.plant,
            health_issues="Test Health Issues",
            part_used="Test Part Used",
            preparation_steps="Test Preparation Steps",
            dosage="Test Dosage",
            contraindications="Test Contraindications",
            shelf_life="Test Shelf Life",
            notes="Test Medicinal Plant Notes",
            contributor=self.user,
        )

        # Create a medicinal plant name for testing
        self.medicinal_plant_name = MedicinalPlantName.objects.create(
            medicinal_plant=self.medicinal_plant,
            language=self.language,
            language_name="Test Language Name",
            plant_name="Test Plant Name",
            is_english=True,
        )

    def test_plant_model(self):
        self.assertEqual(str(self.plant), "Plant: Test Plant")

    def test_plant_name_model(self):
        self.assertEqual(
            str(self.plant_name),
            "Plant Name: Test Plant Name - Language: Test Language Name",
        )

    def test_medicinal_plant_model(self):
        self.assertEqual(
            str(self.medicinal_plant), "Medicinal Info for Plant: Test Plant"
        )

    def test_medicinal_plant_name_model(self):
        self.assertEqual(
            str(self.medicinal_plant_name),
            "Medicinal Plant Name: Test Plant Name - Language: Test Language Name",
        )
