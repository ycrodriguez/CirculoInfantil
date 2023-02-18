from django.db import models
from main.models.room import Room


# Modelo Articulo
class Article(models.Model):
    description_article = models.TextField('Descripción del articulo')
    value = models.FloatField('Valor')
    room_article = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "Articulo " + self.pk
