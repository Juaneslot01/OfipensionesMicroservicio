from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=100)
    acudiente = models.IntegerField(null=False,default=None)
    
    def __str__(self):
        return self.nombre + " " + self.apellido
    
    
    