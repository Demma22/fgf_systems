from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Plant  # Import other models as needed


class PlantViewSetTests(TestCase):
    def setUp(self):
        # Create test data or use fixtures
        self.plant = Plant.objects.create(
            botanical_name="Test Plant", region_in_Uganda="Test Region"
        )
        # Add other setup data as needed
        self.client = APIClient()

    def test_list_plants(self):
        url = reverse("plant-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("count", response.data)
        self.assertIn("plants", response.data)

    def test_review_edit_data(self):
        url = reverse("plant-review-edit-data", args=[self.plant.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add more assertions based on your expected response data

    # Add more tests for other views/actions


# Repeat similar tests for other views and models
