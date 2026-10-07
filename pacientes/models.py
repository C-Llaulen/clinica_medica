from django.db import models

class Paciente(models.Model):
    OPCIONES_GENERO = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    genero = models.CharField(max_length=1, choices=OPCIONES_GENERO)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    diagnostico = models.TextField()
    costo_consulta = models.PositiveIntegerField()
    fecha_ingreso = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre