# Generated by Django 3.1 on 2023-05-11 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appDeshuezadero', '0003_cliente_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='nombre',
        ),
    ]