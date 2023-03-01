from django.contrib import admin
from main.models import *


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['value']
    list_display = ['value']
