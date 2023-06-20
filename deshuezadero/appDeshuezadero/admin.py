from django.contrib import admin
from .models import *

# Register your models here.


class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


class RegionAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


class ComunaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'region')
    search_fields = ('nombre', 'region')


class TipoAdmin(admin.ModelAdmin):
    list_display = ('tipo',)
    search_fields = ('tipo',)


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff')
    search_fields = ('username', 'first_name',
                     'last_name', 'email', 'is_staff')


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'telefono', 'correo',
                    'comuna', 'genero', 'tipo_cliente')
    search_fields = ('rut', 'telefono', 'correo', 'comuna', 'tipo_cliente')


class RepuestoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'tipo_repuesto')
    search_fields = ('nombre', 'precio', 'tipo_repuesto')


class AutoAdmin(admin.ModelAdmin):
    list_display = ('patente', 'marca', 'modelo',
                    'color', 'vendedor', 'vin', 'precio',)
    search_fields = ('patente', 'marca', 'modelo',
                     'color', 'vendedor', 'vin', 'precio',)


class HistorialPagoAdmin(admin.ModelAdmin):
    list_display = ('token', 'cliente', 'tipo_pago', 'valor_neto')
    search_fields = ('token', 'cliente', 'tipo_pago', 'valor_neto')


class ReporteAdmin(admin.ModelAdmin):
    list_display = ('user', 'auto', 'repuesto', 'descripcion', 'razon')
    search_fields = ('user', 'auto', 'repuesto', 'descripcion', 'razon')


class DuenoAutoAdmin(admin.ModelAdmin):
    list_display = ('dueno', 'auto')
    search_fields = ('dueno', 'auto')


class AutoFotosAdmin(admin.ModelAdmin):
    list_display = ('foto', 'auto')
    search_fields = ('foto', 'auto')


class RepuestoFotosAdmin(admin.ModelAdmin):
    list_display = ('foto', 'repuesto')
    search_fields = ('foto', 'repuesto')


admin.site.register(Genero, GeneroAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Comuna, ComunaAdmin)
admin.site.register(TipoCliente, TipoAdmin)
admin.site.register(TipoRepuesto, TipoAdmin)
admin.site.register(TipoPago, TipoAdmin)
admin.site.register(TipoPermiso, TipoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Repuesto, RepuestoAdmin)
admin.site.register(RepuestoFotos, RepuestoFotosAdmin)
admin.site.register(Auto, AutoAdmin)
admin.site.register(AutoFotos, AutoFotosAdmin)
admin.site.register(Reportes, ReporteAdmin)
admin.site.register(HistorialPago, HistorialPagoAdmin)
admin.site.register(DuenoAuto, DuenoAutoAdmin)

admin.site.site_header = 'Administración de Deshuezadero'
admin.site.site_title = 'Administración de Deshuezadero'
admin.site.index_title = 'Administración de Deshuezadero'
