from django.contrib import admin
from .models import Plant, PlantName, MedicinalPlant, MedicinalPlantName, Language

admin.site.register(Plant)
admin.site.register(PlantName)
admin.site.register(MedicinalPlant)
admin.site.register(MedicinalPlantName)
admin.site.register(Language)
