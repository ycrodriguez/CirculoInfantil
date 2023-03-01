from django.contrib import admin
from main.models import *


class ExpedientAdmin(admin.ModelAdmin):
    search_fields = ['code_expedient']
    list_display = ('code_expedient', 'date_letter', 'date_ticket')


admin.site.register(Expedient, ExpedientAdmin)
