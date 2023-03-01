from django.contrib import admin
from main.models import *


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    search_fields = ['code_room', 'room_number']
    list_display = ['code_room', 'room_number']
