# Generated by Django 2.1.2 on 2018-11-25 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eia_app', '0005_auto_20181125_0036'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MedioFisico',
            new_name='Medio',
        ),
        migrations.AddField(
            model_name='caracteristicamedio',
            name='descripcion',
            field=models.TextField(default=''),
        ),
    ]
