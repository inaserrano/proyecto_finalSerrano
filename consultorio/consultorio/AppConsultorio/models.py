from django.db import models

class Turno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    dni = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}" 

class Doctores(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    num_licencia = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    email = models.EmailField()
    dni = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre + " " + self.apellido