# Generated by Django 4.1.7 on 2023-04-05 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_alter_attendance_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='type',
            field=models.CharField(choices=[('ausencia', 'ausencia'), ('tardanza', 'tardanza'), ('vacaciones', 'vacaciones'), ('presente', 'presente')], default='presente', max_length=255, verbose_name='Típo'),
        ),
    ]
