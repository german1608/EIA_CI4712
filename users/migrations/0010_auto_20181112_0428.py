# Generated by Django 2.1.2 on 2018-11-12 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20181109_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True, verbose_name='Dirección de correo electrónico'),
        ),
    ]