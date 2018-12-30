# Generated by Django 2.1.2 on 2018-12-29 21:07

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('medidas', '0003_auto_20181210_0510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medida',
            name='responsable',
        ),
        migrations.AddField(
            model_name='medida',
            name='apellido_responsable',
            field=models.CharField(max_length=100, null=True, verbose_name='Apellido del Responsable'),
        ),
        migrations.AddField(
            model_name='medida',
            name='ci_responsable',
            field=models.CharField(max_length=9, null=True, validators=[django.core.validators.RegexValidator(re.compile('^[V|E|J|P][0-9]{5,9}$'), 'Cédula incorrecta', 'invalid')]),
        ),
        migrations.AddField(
            model_name='medida',
            name='nivel_academico_responsable',
            field=models.DecimalField(decimal_places=4, max_digits=5, null=True, verbose_name='Nivel Académico del Responsable'),
        ),
        migrations.AddField(
            model_name='medida',
            name='nombre_responsable',
            field=models.CharField(max_length=100, null=True, verbose_name='Nombre del Responsable'),
        ),
    ]