# Generated by Django 2.1.2 on 2018-12-10 05:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medidas', '0002_auto_20181126_0438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medida',
            name='apellido_responsable',
        ),
        migrations.RemoveField(
            model_name='medida',
            name='ci_responsable',
        ),
        migrations.RemoveField(
            model_name='medida',
            name='nivel_academico_responsable',
        ),
        migrations.RemoveField(
            model_name='medida',
            name='nombre_responsable',
        ),
        migrations.AddField(
            model_name='medida',
            name='responsable',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Responsable'),
        ),
    ]
