from django.contrib import admin
from main.models import *


class IntoleranceAdmin(admin.ModelAdmin):
    search_fields = ['name_intolerance']
    list_display = ('name_intolerance',)


admin.site.register(Intolerance, IntoleranceAdmin)
