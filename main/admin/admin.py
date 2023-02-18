from django.contrib import admin
from main.models import *


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['value']
    list_display = ('value',)


class ChildAdmin(admin.ModelAdmin):
    search_fields = ['name_child']
    list_display = ('name_child', 'age', 'weight', 'height', 'sexo')


class DiseaseAdmin(admin.ModelAdmin):
    search_fields = ['name_disease']
    list_display = ('name_disease',)


class EconomyAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = ()


class ExpedientAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = ()


class FamilyPickupAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = ()


class IntoleranceAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = ()


class RoomAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = ()


class TutorAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = ()


admin.site.register(Article, ArticleAdmin)
admin.site.register(Child, ChildAdmin)
admin.site.register(Disease)
admin.site.register(Economy)
admin.site.register(Expedient)
admin.site.register(FamilyPickup)
admin.site.register(Intolerance)
admin.site.register(Room)
admin.site.register(Tutor)
