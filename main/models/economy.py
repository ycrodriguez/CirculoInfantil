from django.db import models
from main.models.tutor import Tutor
from main.models.child import Child


# Modelo Economia, datos economicos
class Economy(models.Model):
    tutor = models.OneToOneField(Tutor, on_delete=models.CASCADE)
    members = models.IntegerField('Número de miembros del nucleo familiar')  # Numero de miembros del nucleo familiar

    @property
    def num_chid(self):
        return Child.objects.filter(tutor=self.tutor).count()

    num_chid.fget.short_description = 'Número de niño en el circulo'

    class Meta:
        verbose_name = 'Dato Económico'
        verbose_name_plural = 'Datos Económicos'

    def __str__(self):
        return 'Datos economicos de {}'.format(self.tutor.name_tutor)
