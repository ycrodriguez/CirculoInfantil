from django.db import models
from main.models.child import Child


# Modelo Enfermrdad
class Disease(models.Model):
    code_disease = models.CharField(max_length=8, unique=True)
    name_disease = models.CharField('Nombre de la enfermedad', max_length=16, blank=False, null=False)
    description_disease = models.TextField('Descripción')
    child_disease = models.ManyToManyField(Child, related_name='child_disease')

    def __str__(self):
        return self.name_disease
