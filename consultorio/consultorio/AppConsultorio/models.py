from django.db import models

class Turno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    dni = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}" 
    