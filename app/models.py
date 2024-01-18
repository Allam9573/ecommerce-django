from django.db import models

# Create your models here.


class Producto(models.Model):
    nombre = models.CharField(max_length=60)
    fabricante = models.CharField(max_length=60)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
