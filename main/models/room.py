from django.db import models


# Modelo Salon
class Room(models.Model):
    code_room = models.CharField('Código del Salon', max_length=8, unique=True)
    room_number = models.IntegerField('Número del salon')

    class Meta:
        verbose_name = 'Salon'
        verbose_name_plural = 'Salones'

    def __str__(self):
        return self.code_room
