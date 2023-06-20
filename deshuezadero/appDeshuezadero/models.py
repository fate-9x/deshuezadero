from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
# Create your models here.


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
    rut = models.CharField(max_length=10, null=False, default="0-0")
    telefono = models.CharField(max_length=9, null=True)
    correo = models.CharField(max_length=50, null=False)
    genero = models.ForeignKey(Genero, models.DO_NOTHING, null=True)
    comuna = models.ForeignKey(Comuna, models.DO_NOTHING, null=True)
    tipo_cliente = models.ForeignKey(
        TipoCliente, models.DO_NOTHING)

    def __str__(self):
        return self.rut

    class Meta:
        db_table = 'cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class HistorialPago(models.Model):

    token = models.CharField(max_length=64)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    tipo_pago = models.ForeignKey(TipoPago, models.DO_NOTHING)
    valor_neto = models.IntegerField()

    def __str__(self):
        return self.token

    class Meta:
        db_table = 'historial_pago'
        verbose_name = 'Historial_pago'
        verbose_name_plural = 'Historial_pagos'


class Auto(models.Model):

    patente = models.CharField(max_length=100, null=False, primary_key=True)
    marca = models.CharField(max_length=100, null=False)
    modelo = models.CharField(max_length=100, null=False)
    color = models.CharField(max_length=100, null=False)
    vin = models.CharField(max_length=100, null=True)
    precio = models.IntegerField()
    vendedor = models.ForeignKey(Cliente, models.DO_NOTHING, null=True)

    def __str__(self):
        return self.modelo

    class Meta:
        db_table = 'auto'
        verbose_name = 'Auto'
        verbose_name_plural = 'Autos'


class AutoFotos(models.Model):

    foto = models.ImageField(
        upload_to="uploads/autos", default="/")

    auto = models.ForeignKey(Auto, models.DO_NOTHING)

    class Meta:
        db_table = 'auto_foto'
        verbose_name = 'FotosAutos'
        verbose_name_plural = 'FotosAutos'


class DuenoAuto(models.Model):

    dueno = models.ForeignKey(Cliente, models.DO_NOTHING, null=True)
    auto = models.ForeignKey(Auto, models.DO_NOTHING, null=True)

    def __str__(self):
        return self.dueno

    class Meta:
        db_table = 'dueno_auto'
        verbose_name = 'Dueno_auto'
        verbose_name_plural = 'Duenos_autos'


class Repuesto(models.Model):

    tipo_repuesto = models.ForeignKey(TipoRepuesto, models.DO_NOTHING)
    nombre = models.CharField(max_length=100, null=False)
    precio = models.IntegerField()
    stock = models.IntegerField()
    vendedor = models.ForeignKey(Cliente, models.DO_NOTHING, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'repuesto'
        verbose_name = 'Repuesto'
        verbose_name_plural = 'Repuestos'


class RepuestoFotos(models.Model):
    foto = models.ImageField(
        upload_to="uploads/repuestos", default="/")
    repuesto = models.ForeignKey(Repuesto, models.DO_NOTHING)

    def __str__(self):
        return 'foto'

    class Meta:
        db_table = 'repuesto_foto'
        verbose_name = 'FotoRepuesto'
        verbose_name_plural = 'FotosRepuestos'


class Carrito(models.Model):

    user = models.ForeignKey(Cliente, models.DO_NOTHING, null=True)
    producto = models.ForeignKey(Repuesto, models.DO_NOTHING, null=True)
    auto = models.ForeignKey(Auto, models.DO_NOTHING, null=True)
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


class RazonesReportes(models.Model):

    razon = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.razon

    class Meta:
        db_table = 'razones_reportes'
        verbose_name = 'RazonesReporte'
        verbose_name_plural = 'RazonesReportes'


class Reportes(models.Model):

    user = models.ForeignKey(Cliente, models.DO_NOTHING, null=False)
    auto = models.ForeignKey(Auto, models.DO_NOTHING, null=True)
    repuesto = models.ForeignKey(Repuesto, models.DO_NOTHING, null=True)
    razon = models.ForeignKey(RazonesReportes, models.DO_NOTHING, null=False)
    descripcion = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.descripcion

    class Meta:
        db_table = 'reportes'
        verbose_name = 'Reporte'
        verbose_name_plural = 'Reportes'
