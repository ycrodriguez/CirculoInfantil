from django.db import models
from main.models.child import Child


# Modelo Familiar de Recogida
class FamilyPickup(models.Model):
    code_family = models.CharField(max_length=8, unique=True)
    name_family = models.CharField('Nombre del familiar', max_length=32)
    address_family = models.CharField('Direción del familiar', max_length=128)
    relationship = models.CharField('Parentesco', max_length=32)
    child_family_pickup = models.ManyToManyField(Child, related_name='child_family_pickup')

    def __str__(self):
        return self.name_family
