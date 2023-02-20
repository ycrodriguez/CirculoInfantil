from django.contrib import admin
from main.models import *


class EconomyAdmin(admin.ModelAdmin):
    search_fields = ['tutor']
    list_display = ('tutor',)


admin.site.register(Economy, EconomyAdmin)
