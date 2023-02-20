from django.contrib import admin
from main.models import *


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['value']
    list_display = ('value',)


admin.site.register(Article, ArticleAdmin)
