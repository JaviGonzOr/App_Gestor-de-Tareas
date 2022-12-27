from django.contrib import admin
from .models import Tarea, ImagenTarea, VentasPorMarca, Modelo
from .forms import VentasPorMarcaForm, TareaForm, ModeloForm



class ImagenTareaAdmin (admin.TabularInline):
    model = ImagenTarea

class VentasPorMarcaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
    list_filter = ['nombre']
       

   
class TareaAdmin (admin.ModelAdmin):
    list_display = ['cliente', 'titulo', 'usuario', 'completado']
    search_fields = ['titulo', 'cliente']
    list_filter = ['titulo', 'completado', 'cliente']
    inlines = [
        ImagenTareaAdmin
    ]

class ModeloAdmin(admin.ModelAdmin):
    list_display = ['proveedor','nombre', 'ficha_tecnica']
    list_filter = ['proveedor']





admin.site.register(Tarea, TareaAdmin)
admin.site.register(VentasPorMarca, VentasPorMarcaAdmin)
admin.site.register(Modelo, ModeloAdmin)


