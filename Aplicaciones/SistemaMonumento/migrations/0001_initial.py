# Generated by Django 5.2 on 2025-06-05 18:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=200)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VisitaGuiada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('guia', models.CharField(max_length=100)),
                ('duracion_minutos', models.PositiveIntegerField()),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('monumento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitas', to='SistemaMonumento.monumento')),
            ],
        ),
    ]
