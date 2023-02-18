from django.db import models
from main.models.child import Child


# Modelo Expediente
class Expedient(models.Model):
    code_expedient = models.CharField(max_length=8, unique=True)
    date_letter = models.DateField('Fecha de asignación de la carta', max_length=32)
    date_ticket = models.DateField('Fecha de asignación de la boleta', max_length=32)
    child_expedient = models.OneToOneField(Child, on_delete=models.CASCADE)

    def __str__(self):
        return 'Expediente de ' + self.child_expedient.name_child
