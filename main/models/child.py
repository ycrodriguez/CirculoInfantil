from django.db import models

from main.models.room import Room
from main.models.disease import Disease
from main.models.family_pickup import FamilyPickup
from main.models.intolerance import Intolerance
from main.models.expedient import Expedient
from main.models.choices import SEXO_CHOICES


# Modelo Niño
class Child(models.Model):
    name_child = models.CharField('Nombre y apellidos', max_length=32)
    ci_child = models.CharField('Carne de identidad', max_length=11, unique=True)
    age = models.IntegerField('Edad')
    year = models.IntegerField('Año')
    care_area = models.CharField('Área de atención', max_length=32)
    eyes_color = models.CharField('Color de ojos', max_length=32)
    hair_color = models.CharField('Color del pelo', max_length=32)
    skin_color = models.CharField('Color de piel', max_length=32)
    cp = models.CharField('Consejo popular', max_length=32)
    address_child = models.CharField('Dirección de residencia', max_length=128)
    weight = models.IntegerField('Peso(kg)')
    sexo = models.CharField('Sexo', max_length=10, choices=SEXO_CHOICES, default='female')
    height = models.FloatField('Altura(m)')
    expedient = models.OneToOneField(Expedient, on_delete=models.CASCADE, verbose_name='Expediente')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, verbose_name='Salón')
    diseases = models.ManyToManyField(Disease, verbose_name='Enfermedades', blank=True)
    family_pickup = models.ManyToManyField(FamilyPickup, verbose_name='Familiar de recogida')
    intolerance = models.ManyToManyField(Intolerance, verbose_name='Intolerancias', blank=True)
    tutor = models.ManyToManyField('main.Tutor', verbose_name='Tutor')

    class Meta:
        verbose_name = 'Niño'
        verbose_name_plural = 'Niños'

    def __str__(self):
        return self.name_child
