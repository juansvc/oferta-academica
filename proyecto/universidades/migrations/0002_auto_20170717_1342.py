# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universidades', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='areas',
            options={'managed': False, 'verbose_name_plural': 'Areas'},
        ),
        migrations.AlterModelOptions(
            name='carreras',
            options={'managed': False, 'verbose_name_plural': 'Carreras'},
        ),
        migrations.AlterModelOptions(
            name='carrerasmodalidad',
            options={'managed': False, 'verbose_name_plural': 'Carreras Ofertadas en Modalidades'},
        ),
        migrations.AlterModelOptions(
            name='catalogo',
            options={'managed': False, 'verbose_name_plural': 'Catalogo'},
        ),
        migrations.AlterModelOptions(
            name='detallecatalogo',
            options={'managed': False, 'verbose_name_plural': 'Detalle Catalogo'},
        ),
        migrations.AlterModelOptions(
            name='extension',
            options={'managed': False, 'verbose_name_plural': 'Extension'},
        ),
        migrations.AlterModelOptions(
            name='ies',
            options={'managed': False, 'verbose_name_plural': 'Institucion Educativa Superior'},
        ),
        migrations.AlterModelOptions(
            name='iescarreras',
            options={'managed': False, 'verbose_name_plural': 'Carreras Ofertadas por cada Institucion'},
        ),
        migrations.AlterModelOptions(
            name='matriculados',
            options={'managed': False, 'verbose_name_plural': 'Matriculados por Genero en cada Institucion'},
        ),
        migrations.AlterModelOptions(
            name='matriz',
            options={'managed': False, 'verbose_name_plural': 'Matriz'},
        ),
        migrations.AlterModelOptions(
            name='modalidad',
            options={'managed': False, 'verbose_name_plural': 'Modalidades'},
        ),
        migrations.AlterModelOptions(
            name='nivelformacion',
            options={'managed': False, 'verbose_name_plural': 'Nivel de Formacion'},
        ),
        migrations.AlterModelOptions(
            name='sede',
            options={'managed': False, 'verbose_name_plural': 'Sede'},
        ),
        migrations.AlterModelOptions(
            name='titulados',
            options={'managed': False, 'verbose_name_plural': 'Titulados por Nivel de Formacion Extranjeros y Ecuatorianos'},
        ),
    ]
