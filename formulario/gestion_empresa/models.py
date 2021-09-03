from django.db import models

# Create your models here.

class Persona(models.Model):
    id=models.AutoField(primary_key=True)
    empresa=models.CharField(max_length=50)
    departamento=models.CharField(max_length=20)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    fecha_de_nacimineto=models.DateField()
    correo=models.EmailField(max_length=200)
    telefono=models.CharField(max_length=10)
    fecha_ingrso=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
