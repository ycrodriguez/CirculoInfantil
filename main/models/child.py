from django.db import models
from main.models.room import Room

SEXO_CHOICES = (
    ('female', 'Femenino'),
    ('male', 'Masculino'),
)


# Modelo Niño
class Child(models.Model):
    name_child = models.CharField('Nombre y apellidos', max_length=32)
    ci_child = models.CharField('Carne de identidad', max_length=11, unique=True)
    year = models.IntegerField('Año')
    care_area = models.CharField('Área de atención', max_length=32)
    eyes_color = models.CharField('Color de ojos', max_length=32)
    hair_color = models.CharField('Color del pelo', max_length=32)
    skin_color = models.CharField('Color de piel', max_length=32)
    cp = models.CharField('Consejo popular', max_length=32)
    address_child = models.CharField('Dirección', max_length=128)
    age = models.IntegerField('Edad')
    weight = models.IntegerField('Peso(kg)')
    sexo = models.CharField('Sexo', max_length=10, choices=SEXO_CHOICES, default='female')
    height = models.FloatField('Altura(m)')
    room_child = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name_child
