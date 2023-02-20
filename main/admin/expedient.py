from django.contrib import admin
from main.models import *


class ExpedientAdmin(admin.ModelAdmin):
    search_fields = ['child']
    list_display = ('child', 'date_letter', 'date_ticket')


admin.site.register(Expedient, ExpedientAdmin)
