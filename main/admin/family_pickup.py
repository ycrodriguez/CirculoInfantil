from django.contrib import admin
from main.models import *


class FamilyPickupAdmin(admin.ModelAdmin):
    search_fields = ['name_family']
    list_display = ('name_family', 'relationship')


admin.site.register(FamilyPickup, FamilyPickupAdmin)
