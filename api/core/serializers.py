from rest_framework import serializers
from .models import FichaUsuario

# Serializers define the API representation.
class FichaUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = FichaUsuario
        fields = ['id_usuario','codigo','ddd','telefone','email','senha','tipo_pessoa','nome_fantasia','nome']