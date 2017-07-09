# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.db import models
from django.contrib import admin


class Areas(models.Model):
    nombre = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'areas'
        verbose_name_plural = "Areas"

    def __unicode__(self):
        return "%s" % (self.nombre)


class Carreras(models.Model):
    nombre = models.CharField(unique=True, max_length=200, blank=True, null=True)
    tipo_formacion = models.CharField(max_length=50, blank=True, null=True)
    id_area = models.IntegerField(blank=True, null=True)
    id_nivel = models.ForeignKey('NivelFormacion', db_column='id_nivel', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carreras'
        verbose_name_plural = "Carreras"

    def __unicode__(self):
        return "%s" % (self.nombre)


class CarrerasModalidad(models.Model):
    id_carrera = models.ForeignKey(Carreras, db_column='id_carrera', blank=True, null=True)
    id_modalidad = models.ForeignKey('Modalidad', db_column='id_modalidad', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carreras_modalidad'
        verbose_name_plural = "Carreras Ofertadas en Modalidades"

    def __unicode__(self):
        return "%s - %s" % (self.id_carrera.nombre, self.id_modalidad.nombre)


class Catalogo(models.Model):
    detalle = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogo'
        verbose_name_plural = "Catalogo"

    def __unicode__(self):
        return "%s" % (self.detalle)


class DetalleCatalogo(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)
    id_catalogo = models.ForeignKey(Catalogo, db_column='id_catalogo')
    id_relacion = models.ForeignKey('self', db_column='id_relacion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_catalogo'
        verbose_name_plural = "Detalle Catalogo"

    def __unicode__(self):
        if self.id_relacion == None:
            return "%s - %s" % (self.nombre, self.id_catalogo.detalle)
        else:
            return "%s - %s - %s" % (self.nombre, self.id_relacion.nombre, self.id_catalogo.detalle)


class Extension(models.Model):
    id_ies = models.ForeignKey('Ies', db_column='id_ies', blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=100, blank=True, null=True)
    latitud = models.CharField(max_length=100, blank=True, null=True)
    longitud = models.CharField(max_length=100, blank=True, null=True)
    id_ciudad = models.ForeignKey(DetalleCatalogo, db_column='id_ciudad', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'extension'
        verbose_name_plural = "Extension"

    def __unicode__(self):
        return "%s - %s - %s" % (self.id_ies.nombre, self.id_ciudad.nombre, self.direccion)


class Ies(models.Model):
    acronimo = models.CharField(unique=True, max_length=150, blank=True, null=True)
    nombre = models.CharField(unique=True, max_length=200, blank=True, null=True)
    tipo = models.CharField(max_length=15, blank=True, null=True)
    categoria = models.CharField(max_length=2, blank=True, null=True)
    sitio_web = models.CharField(unique=True, max_length=150, blank=True, null=True)
    total_docentes = models.IntegerField(blank=True, null=True)
    total_docentes_phd = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ies'
        verbose_name_plural = "Institucion Educativa Superior"

    def __unicode__(self):
        return "%s" % (self.nombre)


class IesCarreras(models.Model):
    id_carrera = models.ForeignKey(Carreras, db_column='id_carrera', blank=True, null=True)
    id_ies = models.ForeignKey(Ies, db_column='id_ies', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ies_carreras'
        verbose_name_plural = "Carreras Ofertadas por cada Institucion"

    def __unicode__(self):
        return "%s - %s" % (self.id_ies.nombre, self.id_carrera.nombre)



class Matriculados(models.Model):
    genero = models.CharField(max_length=10, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    id_ies = models.ForeignKey(Ies, db_column='id_ies', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'matriculados'
        verbose_name_plural = "Matriculados por Genero en cada Institucion"

    def __unicode__(self):
        return "%s - %s - %s" % (self.genero, self.id_ies.nombre, self.total)


class Matriz(models.Model):
    id_ies = models.ForeignKey(Ies, db_column='id_ies', blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    latitud = models.CharField(max_length=20, blank=True, null=True)
    longitud = models.CharField(max_length=20, blank=True, null=True)
    id_ciudad = models.ForeignKey(DetalleCatalogo, db_column='id_ciudad', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'matriz'
        verbose_name_plural = "Matriz"

    def __unicode__(self):
        return "%s - %s - %s" % (self.id_ies.nombre, self.id_ciudad.nombre, self.direccion)


class Modalidad(models.Model):
    nombre = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modalidad'
        verbose_name_plural = "Modalidades"

    def __unicode__(self):
        return "%s - %s" % (self.nombre, self.descripcion)


class NivelFormacion(models.Model):
    nivel = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nivel_formacion'
        verbose_name_plural = "Nivel de Formacion"

    def __unicode__(self):
        return "%s - %s" % (self.nivel, self.descripcion)


class Sede(models.Model):
    id_ies = models.ForeignKey(Ies, db_column='id_ies', blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=40, blank=True, null=True)
    latitud = models.CharField(max_length=20, blank=True, null=True)
    longitud = models.CharField(max_length=20, blank=True, null=True)
    id_ciudad = models.ForeignKey(DetalleCatalogo, db_column='id_ciudad', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sede'
        verbose_name_plural = "Sede"

    def __unicode__(self):
        return "%s - %s - %s" % (self.id_ies.nombre, self.id_ciudad.nombre, self.direccion)


class Titulados(models.Model):
    total = models.IntegerField(blank=True, null=True)
    id_nivel = models.ForeignKey(NivelFormacion, db_column='id_nivel', blank=True, null=True)
    id_pais = models.ForeignKey(DetalleCatalogo, db_column='id_pais', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titulados'
        verbose_name_plural = "Titulados por Nivel de Formacion Extranjeros y Ecuatorianos"

    def __unicode__(self):
        return "%s - %s - %s" % (self.id_pais.nombre, self.id_nivel.nivel, self.total)
