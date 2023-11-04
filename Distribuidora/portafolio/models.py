from django.db import models

# Create your models here.

class category(models.Model):
    nombre = models.CharField(max_length=100)
    creado = models.DateTimeField(auto_now_add = True)
    actualizado = models.DateTimeField(auto_now = True )

    class Meta:
        verbose_name = " Categoria "
        verbose_name_plural = "Categorias"
        ordering = ['-creado']

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre_producto = models.CharField (max_length=70)
    precio = models.FloatField()
    descripcion = models.TextField ()
    imagen = models.ImageField (upload_to='projects')
    link=models.URLField (null=True,blank=True)
    categories = models.ManyToManyField(category, related_name="get_posts")
    creado = models.DateTimeField (auto_now_add=True) # añade la fecha automaticamente
    actualizado = models.DateTimeField (auto_now=True) # actualiza la fecha automaticamente

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ['-creado'] #sirve para ordenar del nuevo al antiguo

    def __str__(self): #cambiar el nombre del proyecto
        return self.nombre_producto
    


