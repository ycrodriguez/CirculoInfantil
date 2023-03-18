from django.contrib import admin
from main.models import *


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['name_article']
    list_display = ['name_article', 'description_article', 'value', 'room']
