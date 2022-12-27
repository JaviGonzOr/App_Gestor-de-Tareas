from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TareaForm, VentasPorMarcaForm, ModeloForm
from .models import Tarea, VentasPorMarca, Modelo
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.views.generic import TemplateView

# Create your views here.


def ventas(request):
    labels =  []
    data = []
    
    queryset = VentasPorMarca.objects.order_by('-cantidad')[:15]
    for name in queryset:
        labels.append(name.nombre)
        data.append(name.cantidad)
      

    return render(request, 'ventas.html', {
        'labels' : labels,
        'data' : data,
    })


def home(request):
    return render(request, 'home.html')
     

def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {
            'form': UserCreationForm
        })

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tarea')
            except IntegrityError:
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    'error': 'El Usuario ya existe'
                })

        return render(request, 'registro.html', {
            'form': UserCreationForm,
            'error': 'Las Contraseñas no coinciden'
        })


@login_required
def tarea(request):
    tareas = Tarea.objects.filter(
        usuario=request.user, completado__isnull=True)
    return render(request, 'tarea_pendiente.html', {'tarea': tareas})


@login_required
def tarea_completada(request):
    tareas = Tarea.objects.filter(
        usuario=request.user, completado__isnull=False)
    return render(request, 'tarea_completada.html', {'tarea': tareas})


@login_required
def detalle_tarea(request, tarea_id):
    if request.method == 'GET':
        task = get_object_or_404(Tarea, pk=tarea_id, usuario=request.user)
        form = TareaForm(instance=task)
        return render(request, 'detalle_tarea.html', {'tarea': task, 'form': form})
    else:
        task = get_object_or_404(Tarea, pk=tarea_id, usuario=request.user)
        form = TareaForm(request.POST, instance=task, files=request.FILES)
        form.save()
        return redirect('tarea')


@login_required
def tarea_completa(request, tarea_id):
    task = get_object_or_404(Tarea, pk=tarea_id, usuario=request.user)
    if request.method == 'POST':
        task.completado = timezone.now()
        task.save()
        return redirect('tarea')


@login_required
def tarea_eliminada(request, tarea_id):
    task = get_object_or_404(Tarea, pk=tarea_id, usuario=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tarea_completada')


@login_required
def crear_tarea(request):
    if request.method == 'GET':
        return render(request, 'crear_tarea.html', {
            'form': TareaForm
        })
    else:
        try:
            form = TareaForm(request.POST, files=request.FILES)
            new_task = form.save(commit=False)
            new_task.usuario = request.user
            new_task.save()
            return redirect('tarea')
        except ValueError:
            return render(request, 'crear_tarea.html', {
                'form': TareaForm,
                'error': 'Porfavor, Introduzca datos válidos'
            })


@login_required
def c_sesion(request):
    logout(request)
    return redirect('home')


def i_sesion(request):
    if request.method == 'GET':
        return render(request, 'i_sesion.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'i_sesion.html', {
                'form': AuthenticationForm,
                'error': 'Contraseña o Nombre incorrecto'
            })
        else:
            login(request, user)
            return redirect('tarea')
