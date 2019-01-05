# Generated by Django 2.1.2 on 2018-11-29 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0013_auto_20181116_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=40)),
                ('medidas', models.CharField(default='', max_length=500)),
                ('objetivo_general', models.CharField(default='', max_length=200)),
                ('objetivo_especifico', models.CharField(default='', max_length=500)),
                ('alcance', models.CharField(default='', max_length=200)),
                ('metodologia', models.CharField(default='', max_length=400)),
                ('cronograma', models.CharField(default='', max_length=300)),
                ('responsable', models.CharField(default='', max_length=200)),
                ('costo', models.FloatField()),
                ('proyecto', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='SubPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actividad', models.CharField(default='', max_length=200)),
                ('accion', models.CharField(default='', max_length=200)),
                ('plan', models.CharField(default='', max_length=200)),
                ('monto', models.FloatField()),
                ('plan_principal', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='configuracion.Plan')),
            ],
        ),
        migrations.AddField(
            model_name='actividad',
            name='vulnerabilidades',
            field=models.CharField(default='', max_length=500),
        ),
    ]