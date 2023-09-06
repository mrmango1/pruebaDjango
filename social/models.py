from django.db import models

class Social(models.Model):
    key = models.SlugField(verbose_name="Nombre clave", max_length=50, unique=True)
    name = models.CharField(verbose_name="Red social", max_length=50)
    url = models.URLField(verbose_name="Enlace social", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")
        
    class Meta:
        verbose_name = "Red Social"
        verbose_name_plural = "Redes Sociales"
        ordering = ["name"]
        
    def __str__(self):
        return self.name
