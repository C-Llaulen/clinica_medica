from django import forms
from .models import Paciente

class PacienteCrearForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'rut': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '12345678-9',
                'maxlength': '12',
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. Juan Pérez',
                'maxlength': '30',
            }),
            'edad': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'max': '100',
                'placeholder': 'Ej. 25',
                'oninput': 'if(this.value.length > 3) this.value = this.value.slice(0, 3); if(parseInt(this.value) > 100) this.value = 100;'
            }),
            'genero': forms.Select(attrs={
                'class': 'form-select',
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'nombre@correo.com',
                'maxlength': '40',
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+56912345678',
                'maxlength': '12',
                'oninput': "this.value = this.value.replace(/[^0-9+]/g, '');",
            }),
            'diagnostico': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'maxlength': '500',
                'placeholder': 'Descripción breve...',
            }),
            'costo_consulta': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1000',
                'max': '500000',
                'step': '1000',
                'placeholder': 'Ej. 25000',
                'oninput': 'if(this.value.length > 6) this.value = this.value.slice(0, 6);'
            }),
        }


class PacienteEditarForm(PacienteCrearForm):
    class Meta(PacienteCrearForm.Meta):
        widgets = {
            **PacienteCrearForm.Meta.widgets,
            'rut': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }