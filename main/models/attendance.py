from django.db import models


class Attendance(models.Model):
    child = models.ForeignKey('main.Child', on_delete=models.CASCADE, verbose_name='Niño')
    attendance_date = models.DateTimeField(verbose_name='Día de asistencia ')
    type = models.CharField(max_length=255, default='presente',
                            choices={('presente', 'presente'), ('certificado', 'certificado'),
                                     ('vacaciones', 'vacaciones'),
                                     ('ausencia', 'ausencia')},
                            verbose_name='Típo')
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'

    def __str__(self):
        return 'Asistencia de {} {}'.format(self.child.name_child, self.attendance_date)
