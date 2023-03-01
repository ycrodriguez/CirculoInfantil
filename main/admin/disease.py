from django.contrib import admin
from main.models import *


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    search_fields = ['name_disease']
    list_display = ['name_disease', 'description_disease']
