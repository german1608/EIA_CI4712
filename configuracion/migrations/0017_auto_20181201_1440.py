# Generated by Django 2.0.1 on 2018-12-01 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0016_remove_plan_medidas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planmedidas',
            name='plan_principal',
        ),
        migrations.RemoveField(
            model_name='planobjetivos',
            name='plan_principal',
        ),
        migrations.AddField(
            model_name='plan',
            name='medidas',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='plan',
            name='objetivo_especifico',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.DeleteModel(
            name='PlanMedidas',
        ),
        migrations.DeleteModel(
            name='PlanObjetivos',
        ),
    ]
