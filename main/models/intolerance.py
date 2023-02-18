from django.db import models
from main.models.child import Child


# Modelo Intolerancia
class Intolerance(models.Model):
    code_into = models.CharField(max_length=8, unique=True)
    name_intolerance = models.CharField('Nombre de la intolerancia', max_length=16)
    description_intolerance = models.TextField('Descripción')
    child_intolerance = models.ManyToManyField(Child, related_name='child_intolerance')

    def __str__(self):
        return self.name_intolerance
