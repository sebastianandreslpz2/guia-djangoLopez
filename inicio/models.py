from django.db import models


class Notebook(models.Model):
    modelo = models.CharField(max_length=50)
    procesador = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="imagen_notebooks/", null=True)
    ram = models.CharField(max_length=50, default="Sin especificar")

    def __str__(self):
        return f"notebook ({self.id}): {self.modelo} - {self.procesador}"
    