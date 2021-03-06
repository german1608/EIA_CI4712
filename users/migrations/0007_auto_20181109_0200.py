# Generated by Django 2.1.2 on 2018-11-09 02:00

from django.db import migrations


def crear_grupos(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    roles = ['Administrador del Sistema', 'Solicitante o Promotor', 'Especialista de EsIA',
             'Especialista del Medio Físico', 'Especialista del Medio Biológico',
             'Especialista del Medio Socioeconómico', 'Gerente del Proyecto de desarrollo',
             'Representante legal']
    grupos = map(lambda name: Group(name=name), roles)
    Group.objects.bulk_create(grupos)

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20181108_1841'),
    ]

    operations = [
        migrations.RunPython(crear_grupos)
    ]
