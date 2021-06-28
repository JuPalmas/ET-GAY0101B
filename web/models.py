from django.db import models
from django.utils import timezone

class Post(models.Model):
    autor = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    precio = models.IntegerField()
    imagen = models.ImageField(null=True)
    descripcion = models.TextField()
    regiones = (
        ('I', 'Arica y Parinacota'),
        ('II', 'Antofagasta'),
        ('III', 'Atacama y Coquimbo'),
        ('IV', 'Valparaíso'),
        ('V', '	OHiggins'),
        ('VI', 'Maule'),
        ('VII', 'Biobío'),
        ('VIII', 'La Araucanía'),
        ('IX', 'Los Ríos y Los Lagos'),
        ('X', 'Los Lagos y Aysén'),
        ('XI', 'Magallanes'),
        ('RM', 'Metropolitana de Santiago'),
    )
    region = models.CharField(max_length=4,choices=regiones, blank=True, default='RM', help_text='Región')
    comuna = models.CharField(max_length=50,null=True)
    direccion = models.CharField(max_length=50,null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    estado_publicacion = (
        ('a', 'Disponible'),        
        ('b', 'Agotado'),
        ('c', 'Pausada'),
        ('d', 'No disponible'),
    )
    status = models.CharField(max_length=1, choices=estado_publicacion, blank=True, default='a', help_text='Disponibilidad')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

