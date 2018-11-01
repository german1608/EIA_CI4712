# Generated by Django 2.1.2 on 2018-11-01 01:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('ciudad', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DatosPersona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, validators=[django.core.validators.RegexValidator(re.compile('^[\\w+\\s]+$'), 'Nombre incorrecto', 'invalid')])),
                ('apellido', models.CharField(max_length=60, validators=[django.core.validators.RegexValidator(re.compile('^[\\w+\\s]+$'), 'Apellido incorrecto', 'invalid')])),
                ('cedula', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(re.compile('/^[V|E|J|P][0-9]{5,9}$/'), 'Cédula incorrecta', 'invalid')])),
                ('pasaporte', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='DatosProyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True)),
                ('ubicacion', models.TextField()),
                ('area', models.TextField()),
                ('tipo', models.TextField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Organizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(choices=[('natural', 'Persona natural'), ('juridica', 'Persona Jurídica')], max_length=8)),
                ('nombre', models.CharField(max_length=100)),
                ('rif', models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^([VEJPGvejpg]{1})-([0-9]{8})-([0-9]{1}$)'), 'RIF incorrecto', 'invalid')])),
                ('direccion', models.TextField()),
                ('nombre_representante_legal', models.CharField(max_length=60, validators=[django.core.validators.RegexValidator(re.compile('^[\\w+\\s]+$'), 'Nombre incorrecto', 'invalid')])),
                ('apellido_representante_legal', models.CharField(max_length=60, validators=[django.core.validators.RegexValidator(re.compile('^[\\w+\\s]+$'), 'Apellido incorrecto', 'invalid')])),
                ('cedula_representante_legal', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(re.compile('^[V|E|J|P][0-9]{5,9}$'), 'Cédula incorrecta', 'invalid')])),
                ('pasaporte_representante_legal', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('telefono', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(re.compile('^[0-9]{11}$'), 'Teléfono incorrecto', 'invalid')])),
                ('email', models.EmailField(max_length=254)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eia_app.DatosProyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, validators=[django.core.validators.RegexValidator(re.compile('^[\\w+\\s]+$'), 'Nombre incorrecto', 'invalid')])),
                ('apellido', models.CharField(max_length=60, validators=[django.core.validators.RegexValidator(re.compile('^[\\w+\\s]+$'), 'Apellido incorrecto', 'invalid')])),
                ('cedula', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(re.compile('^[V|E|J|P][0-9]{5,9}$'), 'Cédula incorrecta', 'invalid')])),
                ('pasaporte', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('nivel_academico', models.CharField(max_length=100)),
                ('tipo_responsable', models.CharField(choices=[('EsIA', 'Especialista del EsIA'), ('fisico', 'Especialista del Medio Físico'), ('biologico', 'Especialista del Medio Biológico'), ('socioeconomico', 'Especialista del Medio Socioeconómico'), ('gerente', 'Gerente del Proyecto de Desarrollo')], max_length=16)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eia_app.DatosProyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Solicitante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, validators=[django.core.validators.RegexValidator(re.compile('^[\\w+\\s]+$'), 'Nombre incorrecto', 'invalid')])),
                ('apellido', models.CharField(max_length=60, validators=[django.core.validators.RegexValidator(re.compile('^[\\w+\\s]+$'), 'Apellido incorrecto', 'invalid')])),
                ('cedula', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(re.compile('^[V|E|J|P][0-9]{5,9}$'), 'Cédula incorrecta', 'invalid')])),
                ('pasaporte', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('telefono', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(re.compile('^[0-9]{11}$'), 'Teléfono incorrecto', 'invalid')])),
                ('email', models.EmailField(max_length=254)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eia_app.DatosProyecto')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='datospersona',
            unique_together={('cedula', 'pasaporte')},
        ),
        migrations.AddField(
            model_name='datosdocumento',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eia_app.DatosProyecto'),
        ),
        migrations.AlterUniqueTogether(
            name='solicitante',
            unique_together={('cedula', 'pasaporte')},
        ),
        migrations.AlterUniqueTogether(
            name='responsable',
            unique_together={('cedula', 'pasaporte')},
        ),
    ]
