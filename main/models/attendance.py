from django.db import models


class Attendance(models.Model):
    room = models.ForeignKey('main.Room', on_delete=models.CASCADE)
    child = models.ForeignKey('main.Child', on_delete=models.CASCADE)
    attendance_date = models.DateTimeField()
    type = models.CharField(max_length=255, choices={('1', 'presente'), ('2', 'tardanza'), ('3', 'ausencia')})
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.room.room_number, self.child.name_child)
