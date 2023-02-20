from django.contrib import admin
from main.models import *


class ChildAdmin(admin.ModelAdmin):
    search_fields = ['name_child']
    list_display = ('name_child', 'age', 'weight', 'height', 'sexo')


admin.site.register(Child, ChildAdmin)
