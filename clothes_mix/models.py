from django.db import models

# Create your models here.
  class formulario(models.model):
      rut = models.CharField(max_length=200)