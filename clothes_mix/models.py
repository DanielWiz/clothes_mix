from django.db import models

# Create your models here.
class formulario(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    correo= models.EmailField
    producto=models.CharField(max_length=50)
    telefono= models.CharField(max_length=50)
    direccion= models.CharField(max_length=50)
    sugerencia= models.TextField


def str(self):
        return "%s %s" % (self.nombre,self.apellido)