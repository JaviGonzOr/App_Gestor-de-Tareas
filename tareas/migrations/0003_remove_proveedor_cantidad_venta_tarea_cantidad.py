# Generated by Django 4.1.3 on 2022-12-25 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0002_remove_tarea_cantidad_proveedor_cantidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor',
            name='cantidad',
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(null=True)),
                ('nombre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tareas.modelo')),
                ('proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tareas.proveedor')),
            ],
        ),
        migrations.AddField(
            model_name='tarea',
            name='cantidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tareas.venta'),
        ),
    ]