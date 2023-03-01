from django.contrib import admin
from main.models import *


@admin.register(Economy)
class EconomyAdmin(admin.ModelAdmin):
    search_fields = ['tutor']
    list_display = ['tutor']
