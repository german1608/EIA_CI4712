# Generated by Django 2.1.2 on 2018-11-08 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20181021_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='doc_identidad',
            field=models.CharField(max_length=10),
        ),
    ]