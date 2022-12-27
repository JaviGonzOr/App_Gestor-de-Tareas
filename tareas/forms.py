from django import forms 
from .models import Tarea, VentasPorMarca, Modelo


class TareaForm (forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'proveedor',  'modelo', 'cliente', 'descripcion', 'material', 'importante', 'imagen'] 
        widjets = {
            'titulo': forms.TextInput (attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput (attrs={'class': 'form-control'}),
            'material': forms.Textarea (attrs={'class': 'form-control'}),
            'importante': forms.CheckboxInput (attrs={'class': 'form-check-input'})
        }

class VentasPorMarcaForm (forms.ModelForm):
    class Meta:
        model = VentasPorMarca
        fields = ['nombre']

class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = ['nombre']







