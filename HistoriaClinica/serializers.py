from rest_framework import serializers
from . import models


class HistoriaSerializer(serializers.ModelSerializer):

    class Meta:
        fields =(
            'antecedentesMedicos',
            'medicamentosActuales',
            'alergias',
            'cirugiasPrevias',
            'notasAdicionales',
        )
        model = models.HistoriaClinica