# Generated by Django 2.1.2 on 2018-11-14 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0006_auto_20181114_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='disciplina',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='configuracion.Disciplina'),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='macro',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='configuracion.Macro'),
        ),
    ]