from rest_framework import serializers
from documentos.models import  docAnalisisModel

class doc_analisis_Serializer1(serializers.ModelSerializer):
    class Meta:
        model = docAnalisisModel
        fields = ('__all__')