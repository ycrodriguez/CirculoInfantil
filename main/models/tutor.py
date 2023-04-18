import calendar
from django.db import models
from django.utils import timezone

from main.models.child import Child
from main.models.attendance import Attendance


# Modelo Tutor
class Tutor(models.Model):
    ci_tutor = models.CharField('Carned de identidad', max_length=11, unique=True)
    name_tutor = models.CharField('Nombre', max_length=32)
    workplace = models.CharField('Centro de trabajo', max_length=32)  # Centro de trabajo
    position = models.CharField('Cargo donde trabajo', max_length=32)  # Cargo donde trabajo
    salary = models.FloatField('Salario')
    work_address = models.CharField('Dirección de trabajo', max_length=128)
    tutor_address = models.CharField('Dirección de residencia', max_length=128)
    civil_status = models.CharField('Estado civil', max_length=8)  # Estado Civil
    other_income = models.IntegerField('Otros ingresos')  # Otros Ingresos
    phone = models.CharField('Teléfono', max_length=16)

    class Meta:
        verbose_name = 'Tutor'
        verbose_name_plural = 'Tutores'

    def __str__(self):
        return self.name_tutor

    def chequera(self):
        chequera = 0
        fecha = timezone.now().date()
        calendario = calendar.Calendar().itermonthdays4(fecha.year, fecha.month)
        childs_tutor = Child.objects.filter(tutor__pk=self.pk)
        if childs_tutor.count() == 0:
            return chequera
        if childs_tutor.count() == 1:
            chequera = 40
        if childs_tutor.count() == 2:
            chequera = 30
        if childs_tutor.count() >= 3:
            chequera = 0
            return chequera
        for i in childs_tutor:
            for j in calendario:
                if j[1] == fecha.month and j[2] <= fecha.day and (j[3] != 5 or j[3] != 6):
                    print(i)
                    ausencia = Attendance.objects.filter(child=i, attendance_date__year=j[0],
                                                         attendance_date__month=j[1],
                                                         attendance_date__day=j[2]).order_by(
                        '-attendance_date').first()
                    if ausencia:
                        if ausencia.type == 'certificado' or ausencia.type == 'vacaciones':
                            chequera -= 1.67
        return chequera
