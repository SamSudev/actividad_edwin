from django.db import models
from django.conf import settings

class Tarea(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    importante = models.BooleanField(default=False)  # <-- nuevo campo
    completada = models.BooleanField(default=False)
    creada = models.DateTimeField(auto_now_add=True)
    #vencimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo

