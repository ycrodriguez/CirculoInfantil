from django.contrib import admin
from main.models import *


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    search_fields = ['attendance_date', 'child', 'type']
    list_display = ['attendance_date', 'child', 'type']
