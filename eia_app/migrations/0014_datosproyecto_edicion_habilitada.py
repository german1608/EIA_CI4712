# Generated by Django 2.1.2 on 2018-12-30 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eia_app', '0013_auto_20181229_0213'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosproyecto',
            name='edicion_habilitada',
            field=models.BooleanField(default=False),
        ),
    ]