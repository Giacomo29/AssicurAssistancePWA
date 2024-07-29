from rest_framework import serializers
from assicurassistapp.models import *


class VeicoloSerializer(serializers.ModelSerializer):
    """Serializer for Veicolo model."""
    
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Veicolo
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    """Serializer for Cliente model."""
    
    user = serializers.StringRelatedField(read_only=True)
    veicoli = VeicoloSerializer(many=True, read_only=True)

    class Meta:
        model = Cliente
        fields = '__all__'


class BrokerSerializer(serializers.ModelSerializer):
    """Serializer for Broker model."""
    
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Broker
        fields = '__all__'


class CompagniaSerializer(serializers.ModelSerializer):
    """Serializer for Compagnia model."""
    
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Compagnia
        fields = '__all__'


class ClienteListSerializer(serializers.ModelSerializer):
    """Serializer for listing clients."""
    
    class Meta:
        model = Cliente
        fields = ('cognome', 'nome', 'codice_fiscale')


class DocumentoSerializer(serializers.ModelSerializer):
    """Serializer for Documento model."""
    
    class Meta:
        model = Documento
        fields = ('id', 'polizza', 'file',)


class PolizzaSerializer(serializers.ModelSerializer):
    """Serializer for Polizza model."""
    
    user = serializers.StringRelatedField(read_only=True)
    cliente = ClienteListSerializer(read_only=True)
    intestatario = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all(), write_only=True)
    documenti = DocumentoSerializer(many=True, read_only=True, required=False)
    uploaded_documents = serializers.ListField(
        child=serializers.FileField(allow_empty_file=False, max_length=100000, use_url=False,),
        required=False,
        write_only=True
    )

    class Meta:
        model = Polizza
        fields = ('id_polizza','user','cliente','compagnia','note','semestrale','data_inizio','data_fine','data_fine_due','premio','veicolo', 'intestatario','documenti','uploaded_documents')

    def create(self, validated_data):
        """Method to create Polizza instance."""

        uploaded_documents = validated_data.pop('uploaded_documents', [])
        cliente_data = validated_data.pop('intestatario')
        cliente = Cliente.objects.get(pk=cliente_data.pk)
        polizza = Polizza.objects.create(cliente=cliente, **validated_data)
        for file in uploaded_documents:
            Documento.objects.create(polizza=polizza, file=file)
        return polizza

