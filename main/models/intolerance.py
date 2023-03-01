from django.db import models


# Modelo Intolerancia
class Intolerance(models.Model):
    code_into = models.CharField(max_length=8, unique=True)
    name_intolerance = models.CharField('Nombre de la intolerancia', max_length=16)
    description_intolerance = models.TextField('Descripción')

    class Meta:
        verbose_name = 'Intolerancia'
        verbose_name_plural = 'Intolerancias'

    def __str__(self):
        return self.name_intolerance    
