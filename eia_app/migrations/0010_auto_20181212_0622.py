# Generated by Django 2.1.2 on 2018-12-12 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eia_app', '0009_auto_20181212_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conclusionproyecto',
            name='proyecto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='eia_app.DatosProyecto'),
        ),
        migrations.AlterField(
            model_name='recomendacionproyecto',
            name='proyecto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='eia_app.DatosProyecto'),
        ),
    ]