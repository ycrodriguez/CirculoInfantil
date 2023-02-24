from django.db import models


# Modelo Expediente
class Expedient(models.Model):
    code_expedient = models.CharField('Codigo del expediente', max_length=8, unique=True)
    date_letter = models.DateField('Fecha de asignación de la carta', max_length=32)
    date_ticket = models.DateField('Fecha de asignación de la boleta', max_length=32)

    class Meta:
        verbose_name = 'Expediente'
        verbose_name_plural = 'Expedientes'

    def __str__(self):
        return 'Expediente' + self.code_expedient
