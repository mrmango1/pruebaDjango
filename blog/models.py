from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Crea tus modelos aquí.
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Título")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["-created"]
    
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nombre de la Categoria")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de Publicación", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blogs")
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE) # uno a varios
    categories = models.ManyToManyField(Category, verbose_name="Categorías")# muchos a muchos 
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")
    
    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ["title"]
        
    def __str__(self):
        return self.title
