# Generated by Django 3.1 on 2023-05-15 21:49

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('vin', models.CharField(max_length=100, null=True)),
                ('patente', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Auto',
                'verbose_name_plural': 'Autos',
                'db_table': 'auto',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=9, null=True)),
                ('correo', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'cliente',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='nombre')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
                'db_table': 'estado',
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Genero',
                'verbose_name_plural': 'Generos',
                'db_table': 'genero',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regiones',
                'db_table': 'region',
            },
        ),
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Repuesto',
                'verbose_name_plural': 'Repuestos',
                'db_table': 'repuesto',
            },
        ),
        migrations.CreateModel(
            name='TipoCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tipo_cliente',
                'verbose_name_plural': 'Tipos_cliente',
                'db_table': 'tipo_cliente',
            },
        ),
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tipo_pago',
                'verbose_name_plural': 'Tipo_pagos',
                'db_table': 'tipo_pago',
            },
        ),
        migrations.CreateModel(
            name='TipoPermiso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tipo_permiso',
                'verbose_name_plural': 'Tipos_permisos',
                'db_table': 'tipo_permiso',
            },
        ),
        migrations.CreateModel(
            name='TipoRepuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tipo_repuesto',
                'verbose_name_plural': 'Tipos_repuestos',
                'db_table': 'tipo_repuesto',
            },
        ),
        migrations.CreateModel(
            name='RepuestoFotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(default='/', upload_to='uploads/repuestos')),
                ('repuesto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='appDeshuezadero.repuesto')),
            ],
            options={
                'verbose_name': 'FotoRepuesto',
                'verbose_name_plural': 'FotosRepuestos',
                'db_table': 'repuesto_foto',
            },
        ),
        migrations.AddField(
            model_name='repuesto',
            name='tipo_repuesto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='appDeshuezadero.tiporepuesto'),
        ),
        migrations.AddField(
            model_name='repuesto',
            name='vendedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appDeshuezadero.cliente'),
        ),
        migrations.CreateModel(
            name='PermisoCirculacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_permiso', models.CharField(max_length=50)),
                ('auto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appDeshuezadero.auto')),
            ],
            options={
                'verbose_name': 'PermisoCirculacion',
                'verbose_name_plural': 'PermisosCirculacion',
                'db_table': 'permiso_circulacion',
            },
        ),
        migrations.CreateModel(
            name='HistorialPago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64)),
                ('valor_neto', models.CharField(max_length=11)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='appDeshuezadero.cliente')),
                ('tipo_pago', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='appDeshuezadero.tipopago')),
            ],
            options={
                'verbose_name': 'Historial_pago',
                'verbose_name_plural': 'Historial_pagos',
                'db_table': 'historial_pago',
            },
        ),
        migrations.CreateModel(
            name='DuenoAuto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appDeshuezadero.auto')),
                ('dueno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appDeshuezadero.cliente')),
            ],
            options={
                'verbose_name': 'Dueno_auto',
                'verbose_name_plural': 'Duenos_autos',
                'db_table': 'dueno_auto',
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='appDeshuezadero.region')),
            ],
            options={
                'verbose_name': 'Comuna',
                'verbose_name_plural': 'Comunas',
                'db_table': 'comuna',
            },
        ),
        migrations.AddField(
            model_name='cliente',
            name='comuna',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appDeshuezadero.comuna'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='genero',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appDeshuezadero.genero'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='tipo_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='appDeshuezadero.tipocliente'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('precio', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('suma', models.IntegerField()),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appDeshuezadero.repuesto')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appDeshuezadero.cliente')),
            ],
            options={
                'verbose_name': 'carrito',
                'verbose_name_plural': 'carritos',
                'db_table': 'Carrito',
            },
        ),
    ]
