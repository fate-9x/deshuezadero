# Generated by Django 3.1 on 2023-05-14 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDeshuezadero', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='nombre',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
