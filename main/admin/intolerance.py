from django.contrib import admin
from main.models import *


@admin.register(Intolerance)
class IntoleranceAdmin(admin.ModelAdmin):
    search_fields = ['name_intolerance']
    list_display = ['name_intolerance', 'description_intolerance']
