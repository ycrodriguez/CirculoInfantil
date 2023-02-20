from django.contrib import admin
from main.models import *


class TutorAdmin(admin.ModelAdmin):
    search_fields = ['name_tutor']
    list_display = ('name_tutor', 'workplace', 'salary')


admin.site.register(Tutor, TutorAdmin)
