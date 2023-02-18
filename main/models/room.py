from django.db import models


# Modelo Salon
class Room(models.Model):
    code_room = models.CharField(max_length=8, unique=True)
    room_number = models.IntegerField('Número del salon')

    def __str__(self):
        return self.code_room
