# Generated by Django 4.1.3 on 2022-12-24 12:16

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
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('ficha_tecnica', models.FileField(null=True, upload_to='Chimeneas')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('cliente', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('material', models.TextField(blank=True)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('completado', models.DateTimeField(blank=True, null=True)),
                ('importante', models.BooleanField(default=True)),
                ('imagen', models.FileField(null=True, upload_to='Chimeneas')),
                ('cantidad', models.PositiveIntegerField(null=True)),
                ('modelo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tareas.modelo')),
                ('proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tareas.proveedor')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='modelo',
            name='proveedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tareas.proveedor'),
        ),
        migrations.CreateModel(
            name='ImagenTarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='Chimeneas')),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tareas.tarea')),
            ],
        ),
    ]