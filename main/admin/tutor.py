from django.contrib import admin
from main.models import *


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    search_fields = ['name_tutor']
    list_display = ['name_tutor', 'tutor_address', 'workplace', 'salary', 'chequera']
