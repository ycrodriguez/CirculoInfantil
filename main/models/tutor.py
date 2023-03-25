from django.db import models


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
        return 0