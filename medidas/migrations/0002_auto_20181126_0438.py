# Generated by Django 2.1.2 on 2018-11-26 04:38

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('medidas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medida',
            name='ci_responsable',
            field=models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(re.compile('^[V|E|J|P][0-9]{5,9}$'), 'Cédula incorrecta', 'invalid')]),
        ),
    ]
