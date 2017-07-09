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


class Areas(models.Model):
    nombre = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'areas'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Carreras(models.Model):
    nombre = models.CharField(unique=True, max_length=200, blank=True, null=True)
    tipo_formacion = models.CharField(max_length=50, blank=True, null=True)
    id_area = models.IntegerField(blank=True, null=True)
    id_nivel = models.ForeignKey('NivelFormacion', db_column='id_nivel', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carreras'


class CarrerasModalidad(models.Model):
    id_carrera = models.ForeignKey(Carreras, db_column='id_carrera', blank=True, null=True)
    id_modalidad = models.ForeignKey('Modalidad', db_column='id_modalidad', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carreras_modalidad'


class Catalogo(models.Model):
    detalle = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogo'


class DetalleCatalogo(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)
    id_catalogo = models.ForeignKey(Catalogo, db_column='id_catalogo')
    id_relacion = models.ForeignKey('self', db_column='id_relacion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_catalogo'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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


class IesCarreras(models.Model):
    id_carrera = models.ForeignKey(Carreras, db_column='id_carrera', blank=True, null=True)
    id_ies = models.ForeignKey(Ies, db_column='id_ies', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ies_carreras'


class Matriculados(models.Model):
    genero = models.CharField(max_length=10, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    id_ies = models.ForeignKey(Ies, db_column='id_ies', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'matriculados'


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


class Modalidad(models.Model):
    nombre = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modalidad'


class NivelFormacion(models.Model):
    nivel = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nivel_formacion'


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


class Titulados(models.Model):
    total = models.IntegerField(blank=True, null=True)
    id_nivel = models.ForeignKey(NivelFormacion, db_column='id_nivel', blank=True, null=True)
    id_pais = models.ForeignKey(DetalleCatalogo, db_column='id_pais', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titulados'
