# Generated by Django 2.0.1 on 2018-12-01 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0017_auto_20181201_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanMedidas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medidas', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='PlanObjetivos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objetivo_especifico', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='plan',
            name='medidas',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='objetivo_especifico',
        ),
        migrations.AddField(
            model_name='planobjetivos',
            name='plan_principal',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='configuracion.Plan'),
        ),
        migrations.AddField(
            model_name='planmedidas',
            name='plan_principal',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='configuracion.Plan'),
        ),
    ]
