# Generated by Django 4.1.3 on 2022-12-26 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0009_remove_proveedor_cantidad_tarea_cantidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='cantidad',
        ),
        migrations.AddField(
            model_name='proveedor',
            name='cantidad',
            field=models.PositiveIntegerField(null=True),
        ),
    ]