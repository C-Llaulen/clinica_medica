from rest_framework import serializers
from .models import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = [
            'id',
            'rut',
            'nombre',
            'edad',
            'genero',
            'correo',
            'telefono',
            'diagnostico',
            'costo_consulta',
            'fecha_ingreso',
        ]
        read_only_fields = ['id', 'fecha_ingreso']

    def validate_edad(self, value):
        if value < 0 or value > 100:
            raise serializers.ValidationError("La edad debe estar comprendida entre 0 y 100 años.")
        return value

    def validate_costo_consulta(self, value):
        if value < 1000 or value > 500000:
            raise serializers.ValidationError("El costo de la consulta debe estar entre $1.000 y $500.000.")
        return value