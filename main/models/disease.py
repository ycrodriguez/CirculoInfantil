from django.db import models


# Modelo Enfermrdad
class Disease(models.Model):
    code_disease = models.CharField(verbose_name='Código de Enfermedades', max_length=8, unique=True)
    name_disease = models.CharField('Nombre de la enfermedad', max_length=16)
    description_disease = models.TextField('Descripción')

    class Meta:
        verbose_name = 'Enfermedad'
        verbose_name_plural = 'Enfermedades'

    def __str__(self):
        return self.name_disease
