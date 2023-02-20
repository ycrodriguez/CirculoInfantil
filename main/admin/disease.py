from django.contrib import admin
from main.models import *


class DiseaseAdmin(admin.ModelAdmin):
    search_fields = ['name_disease']
    list_display = ('name_disease',)


admin.site.register(Disease, DiseaseAdmin)
