from django.db import models


# Create your models here.
class Formulario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(null=True)
    producto = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    sugerencia = models.TextField(null=True)

    def __str__(self):
        return "%s %s" % (self.nombre, self.apellido)

class Ropa(models.Model):
    nombre = models.CharField(max_length=10, unique=True)
    imagen = models.ImageField(upload_to="ropas", null=True)
    def __str__(self):
        return self.nombre

        