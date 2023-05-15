from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
# Create your models here.


class Estado(models.Model):
    # id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='nombre')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'estado'
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'


class Genero(models.Model):
    nombre = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'genero'
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'


class Region(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'region'
        verbose_name = 'Region'
        verbose_name_plural = 'Regiones'


class Comuna(models.Model):
    nombre = models.CharField(max_length=50)
    region = models.ForeignKey(Region, models.DO_NOTHING)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'comuna'
        verbose_name = 'Comuna'
        verbose_name_plural = 'Comunas'


class TipoCliente(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo

    class Meta:
        db_table = 'tipo_cliente'
        verbose_name = 'Tipo_cliente'
        verbose_name_plural = 'Tipos_cliente'


class TipoRepuesto(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo

    class Meta:
        db_table = 'tipo_repuesto'
        verbose_name = 'Tipo_repuesto'
        verbose_name_plural = 'Tipos_repuestos'


class TipoPermiso(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo

    class Meta:
        db_table = 'tipo_permiso'
        verbose_name = 'Tipo_permiso'
        verbose_name_plural = 'Tipos_permisos'


class TipoPago(models.Model):

    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo

    class Meta:
        db_table = 'tipo_pago'
        verbose_name = 'Tipo_pago'
        verbose_name_plural = 'Tipo_pagos'


class Cliente(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, null=False)
    telefono = models.CharField(max_length=9, null=True)
    correo = models.CharField(max_length=50, null=False)
    genero = models.ForeignKey(Genero, models.DO_NOTHING, null=True)
    comuna = models.ForeignKey(Comuna, models.DO_NOTHING, null=True)
    tipo_cliente = models.ForeignKey(TipoCliente, models.DO_NOTHING, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class HistorialPago(models.Model):

    token = models.CharField(max_length=64)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    tipo_pago = models.ForeignKey(TipoPago, models.DO_NOTHING)
    valor_neto = models.CharField(max_length=11, null=False)

    def __str__(self):
        return self.cliente

    class Meta:
        db_table = 'historial_pago'
        verbose_name = 'Historial_pago'
        verbose_name_plural = 'Historial_pagos'


class Auto(models.Model):

    marca = models.CharField(max_length=100, null=False)
    modelo = models.CharField(max_length=100, null=False)
    color = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.modelo

    class Meta:
        db_table = 'auto'
        verbose_name = 'Auto'
        verbose_name_plural = 'Autos'


class DuenoAuto(models.Model):

    dueno = models.ForeignKey(Cliente, models.DO_NOTHING, null=True)
    auto = models.ForeignKey(Auto, models.DO_NOTHING, null=True)

    def __str__(self):
        return self.dueno

    class Meta:
        db_table = 'dueno_auto'
        verbose_name = 'Dueno_auto'
        verbose_name_plural = 'Duenos_autos'


class Patente(models.Model):

    patente = models.CharField(max_length=6, null=False)
    auto = models.ForeignKey(Auto, models.DO_NOTHING, null=True)

    def __str__(self):
        return self.patente

    class Meta:
        db_table = 'patente'
        verbose_name = 'Patente'
        verbose_name_plural = 'Patentes'


class Repuesto(models.Model):

    tipo_repuesto = models.ForeignKey(TipoRepuesto, models.DO_NOTHING)
    nombre = models.CharField(max_length=100, null=False)
    auto = models.ForeignKey(Auto, models.DO_NOTHING, null=True)
    precio = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'repuesto'
        verbose_name = 'Repuesto'
        verbose_name_plural = 'Repuestos'


class PermisoCirculacion(models.Model):

    tipo_permiso = models.CharField(max_length=50, null=False)
    auto = models.ForeignKey(Auto, models.DO_NOTHING, null=True)

    def __str__(self):
        return self.tipo_permiso

    class Meta:
        db_table = 'permiso_circulacion'
        verbose_name = 'PermisoCirculacion'
        verbose_name_plural = 'PermisosCirculacion'


class Carrito(models.Model):

    user = models.ForeignKey(Cliente, models.DO_NOTHING, null=True)
    producto = models.ForeignKey(Repuesto, models.DO_NOTHING, null=True)
    nombre = models.CharField(max_length=100, null=True)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    suma = models.IntegerField()

    def __str__(self):
        return self.suma

    class Meta:
        db_table = 'Carrito'
        verbose_name = 'carrito'
        verbose_name_plural = 'carritos'
