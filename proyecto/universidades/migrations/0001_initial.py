# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, unique=True, null=True, blank=True)),
            ],
            options={
                'db_table': 'areas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Carreras',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200, unique=True, null=True, blank=True)),
                ('tipo_formacion', models.CharField(max_length=50, null=True, blank=True)),
                ('id_area', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'carreras',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CarrerasModalidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'carreras_modalidad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Catalogo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('detalle', models.CharField(max_length=25, null=True, blank=True)),
            ],
            options={
                'db_table': 'catalogo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleCatalogo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'db_table': 'detalle_catalogo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Extension',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direccion', models.CharField(max_length=200, null=True, blank=True)),
                ('telefono', models.CharField(max_length=100, null=True, blank=True)),
                ('latitud', models.CharField(max_length=100, null=True, blank=True)),
                ('longitud', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'db_table': 'extension',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acronimo', models.CharField(max_length=150, unique=True, null=True, blank=True)),
                ('nombre', models.CharField(max_length=200, unique=True, null=True, blank=True)),
                ('tipo', models.CharField(max_length=15, null=True, blank=True)),
                ('categoria', models.CharField(max_length=2, null=True, blank=True)),
                ('sitio_web', models.CharField(max_length=150, unique=True, null=True, blank=True)),
                ('total_docentes', models.IntegerField(null=True, blank=True)),
                ('total_docentes_phd', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'ies',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IesCarreras',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'ies_carreras',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Matriculados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genero', models.CharField(max_length=10, null=True, blank=True)),
                ('total', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'matriculados',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Matriz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direccion', models.CharField(max_length=200, null=True, blank=True)),
                ('telefono', models.CharField(max_length=20, null=True, blank=True)),
                ('latitud', models.CharField(max_length=20, null=True, blank=True)),
                ('longitud', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'db_table': 'matriz',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Modalidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20, null=True, blank=True)),
                ('descripcion', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'db_table': 'modalidad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NivelFormacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nivel', models.CharField(max_length=20, null=True, blank=True)),
                ('descripcion', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'db_table': 'nivel_formacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direccion', models.CharField(max_length=200, null=True, blank=True)),
                ('telefono', models.CharField(max_length=40, null=True, blank=True)),
                ('latitud', models.CharField(max_length=20, null=True, blank=True)),
                ('longitud', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'db_table': 'sede',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Titulados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'titulados',
                'managed': False,
            },
        ),
    ]
