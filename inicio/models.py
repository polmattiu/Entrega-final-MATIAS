from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

    

class Gasto(models.Model):
    tipo=models.CharField(max_length=40)
    articulo=models.CharField(max_length=20)
    descripcion=RichTextField()
    cantidad=models.IntegerField()
    fecha_de_compra=models.DateField()
    precio = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.tipo} - {self.articulo} -   "
    
    
    
    