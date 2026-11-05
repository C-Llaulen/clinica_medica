from django import forms
from .models import Paciente


class PacienteCrearForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'rut', 'nombre', 'edad', 'genero',
            'telefono', 'correo', 'diagnostico', 'costo_consulta'
        ]
        widgets = {
            'rut': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '12345678-9',
                'maxlength': '10',
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Juan Pérez',
                'maxlength': '20',
            }),
            'edad': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'max': '100',
                'placeholder': '0 - 100',
            }),
            'genero': forms.Select(attrs={
                'class': 'form-select',
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '912345678',
                'maxlength': '9',
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'nombre@correo.cl',
                'maxlength': '35',
            }),
            'costo_consulta': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1000',
                'max': '500000',
                'placeholder': '1000 - 500000',
            }),
            'diagnostico': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descripción del diagnóstico...',
                'maxlength': '250',
            }),
        }


class PacienteEditarForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'rut', 'nombre', 'edad', 'genero',
            'telefono', 'correo', 'diagnostico', 'costo_consulta'
        ]
        widgets = {
            'rut': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '12345678-9',
                'maxlength': '10',
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Juan Pérez',
                'maxlength': '20',
            }),
            'edad': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'max': '100',
                'placeholder': '0 - 100',
            }),
            'genero': forms.Select(attrs={
                'class': 'form-select',
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '912345678',
                'maxlength': '9',
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'nombre@correo.cl',
                'maxlength': '25',
            }),
            'costo_consulta': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1000',
                'max': '500000',
                'placeholder': '1000 - 500000',
            }),
            'diagnostico': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descripción del diagnóstico...',
                'maxlength': '250',
            }),
        }