from django.db import models


# Modelo Familiar de Recogida
class FamilyPickup(models.Model):
    code_family = models.CharField(max_length=8, unique=True)
    name_family = models.CharField('Nombre y apellidos del familiar', max_length=32)
    address_family = models.CharField('Direción del familiar', max_length=128)
    relationship = models.CharField('Parentesco', max_length=32)

    class Meta:
        verbose_name = 'Familiar de Recogida'
        verbose_name_plural = 'Familiares de Recogida'

    def __str__(self):
        return self.name_family
