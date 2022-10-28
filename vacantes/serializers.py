from rest_framework import serializers
from . import models

class VacanteServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Vacante
        fields='__all__'