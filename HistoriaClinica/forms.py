from django import forms
from .models import HistoriaClinica

class HistoriaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = [
            'antecedentesMedicos',
            'medicamentosActuales',
            'alergias',
            'cirugiasPrevias',
            'notasAdicionales',
        ]
        labels = {
            'antecedentesMedicos': 'Antecedentes Médicos',
            'medicamentosActuales': 'Medicamentos Actuales',
            'alergias': 'Alergias',
            'cirugiasPrevias': 'Cirugías Previas',
            'notasAdicionales': 'Notas Adicionales',
        }