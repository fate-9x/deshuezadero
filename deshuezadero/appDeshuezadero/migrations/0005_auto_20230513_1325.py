# Generated by Django 3.1 on 2023-05-13 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appDeshuezadero', '0004_remove_cliente_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='tipo_cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appDeshuezadero.tipocliente'),
        ),
    ]
