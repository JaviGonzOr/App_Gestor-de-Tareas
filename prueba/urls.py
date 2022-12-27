"""prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tareas import views 
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path ('admin/', admin.site.urls),
    path ('', views.home, name='home'),
    path ('registro/', views.registro, name='registro'),
    path ('ventas/', views.ventas, name ='ventas'),
    path ('tarea/', views.tarea, name = 'tarea'),
    path ('tarea/completada/', views.tarea_completada, name = 'tarea_completada'),
    path ('c_sesion/', views.c_sesion, name = 'c_sesion'),
    path ('i_sesion/', views.i_sesion, name = 'i_sesion'),
    path ('tarea/crear/', views.crear_tarea, name = 'crear_tarea'),
    path ('tarea/<int:tarea_id>/', views.detalle_tarea, name = 'detalle_tarea'),
    path ('tarea/<int:tarea_id>/completado', views.tarea_completa, name = 'tarea_completa'),
    path ('tarea/<int:tarea_id>/eliminado', views.tarea_eliminada, name = 'tarea_eliminada'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
