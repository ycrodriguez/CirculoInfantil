from django.contrib import admin

from main.models import *
from main.admin.forms.child import ChildForm


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    search_fields = ['name_child']
    list_display = ['name_child', 'age', 'weight', 'height', 'sexo', 'room', 'year', 'expedient']
    form = ChildForm
