from django.db import models
from django.contrib.auth.models import User


# Create your models here.


    

class VentasPorMarca(models.Model):
    nombre = models.CharField(max_length = 25)
    cantidad = models.PositiveIntegerField(null=True)
    
    def __str__(self):
        return f'{self.nombre}'



class Modelo(models.Model):
    nombre = models.CharField(max_length = 40)
    proveedor = models.ForeignKey(VentasPorMarca, null=True, on_delete=models.PROTECT)
    ficha_tecnica = models.FileField(upload_to='Chimeneas', null=True)
    
    
    def __str__(self):
        return self.nombre



class Tarea (models.Model):
    titulo = models.CharField(max_length=100)
    cliente= models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    material = models.TextField(blank=True)
    creacion = models.DateTimeField(auto_now_add = True)
    completado= models.DateTimeField(null=True, blank=True)
    importante = models.BooleanField (default =True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.FileField(upload_to= "Chimeneas", null=True)
    proveedor = models.ForeignKey(VentasPorMarca, null=True, on_delete = models.PROTECT) 
    modelo = models.ForeignKey(Modelo, null=True, on_delete = models.PROTECT)
    
   
    
    def __str__(self):
        return self.titulo + ' - Montador : ' + self.usuario.username





class ImagenTarea (models.Model):
    imagen = models.ImageField (upload_to = "Chimeneas")
    tarea = models.ForeignKey(Tarea, on_delete = models.CASCADE)
    

      
    
