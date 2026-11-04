from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

class Paciente(models.Model):
    OPCIONES_GENERO = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    validador_rut = RegexValidator(
        regex=r'^\d{1,2}\.?\d{3}\.?\d{3}-[\dkK]$',
        message='El RUT debe tener un formato válido (ej: 12345678-9 o 12.345.678-K).'
    )

    validador_telefono = RegexValidator(
        regex=r'^(\+?56)?(\s?)(0?9)(\s?)[0-9]{8}$',
        message='El teléfono debe ser un móvil válido de Chile (ej: 912345678 o +56912345678).'
    )

    rut = models.CharField(max_length=12, unique=True, validators=[validador_rut], verbose_name="RUT")
    nombre = models.CharField(max_length=30, verbose_name="Nombre Completo")
    edad = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0, message="La edad no puede ser menor a 0."),
            MaxValueValidator(100, message="La edad no puede ser mayor a 100 años.")
        ],
        verbose_name="Edad"
    )
    genero = models.CharField(max_length=1, choices=OPCIONES_GENERO, verbose_name="Género")
    correo = models.EmailField(max_length=40, verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=12, validators=[validador_telefono], verbose_name="Teléfono")
    diagnostico = models.TextField(max_length=500, verbose_name="Diagnóstico")
    costo_consulta = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1000, message="El costo de la consulta debe ser de al menos $1.000."),
            MaxValueValidator(500000, message="El costo de la consulta no puede superar los $500.000.")
        ],
        verbose_name="Costo de Consulta"
    )
    fecha_ingreso = models.DateField(auto_now_add=True, verbose_name="Fecha de Ingreso")

    def __str__(self):
        return f"{self.nombre} ({self.rut})"