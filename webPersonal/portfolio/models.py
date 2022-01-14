from django.db import models
from django.db.models.fields import URLField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200,verbose_name = 'titulo')
    desccription = models.TextField(verbose_name = 'descripcion')
    image = models.ImageField(verbose_name = 'imagen', upload_to = 'projects')
    url = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name = 'fecha creacion')
    updated = models.DateTimeField(auto_now_add=True,verbose_name = 'fecha actualizacion')

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']

    def __str__(self):
        return self.title
    