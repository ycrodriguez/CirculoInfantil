from django.contrib import admin
from main.models import *


class RoomAdmin(admin.ModelAdmin):
    search_fields = ['room_number']
    list_display = ('room_number',)


admin.site.register(Room, RoomAdmin)
