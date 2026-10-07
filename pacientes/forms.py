from django import forms
from .models import Paciente


class PacienteCrearForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['rut', 'nombre', 'edad', 'genero', 'correo', 'telefono', 'diagnostico', 'costo_consulta']


class PacienteEditarForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'edad', 'genero', 'correo', 'telefono', 'diagnostico', 'costo_consulta']