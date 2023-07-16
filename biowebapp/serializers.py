from rest_framework import serializers
from .models import *


#serializers for the models
class PfamDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PfamDescription
        fields = ['domain_id', 'domain_description']

class DomainSerializer(serializers.ModelSerializer):
    domain = PfamDescriptionSerializer(read_only=True)

    class Meta:
        model = Domain
        fields = ['domain']


class OrganismSerializer(serializers.ModelSerializer):
    clade = serializers.SerializerMethodField()

    class Meta:
        model = Organism
        fields = ['taxa_id', 'clade', 'genus', 'species']

    def get_clade(self, obj):
        
        return obj.proteins.first().clade if obj.proteins.exists() else None


class SequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sequence
        fields = ['sequence']

class ProteinSerializer(serializers.ModelSerializer):
    taxa = OrganismSerializer(read_only=True)
    domains = DomainSerializer(many=True, read_only=True)
    sequence = SequenceSerializer(read_only=True)

    class Meta:
        model = Protein
        fields = ['protein_id', 'sequence', 'taxa', 'length',
                  'domains', 'description', 'start', 'stop']
# Serializer to create a list of proteins


class ProteinListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protein
        fields = ['protein_id']

class TaxaPfamSerializer(serializers.ModelSerializer):
    pfam_id = PfamDescriptionSerializer(source='domain')

    class Meta:
        model = Domain
        fields = ['pfam_id']

class ProteinCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protein
        fields = ['protein_id', 'taxa', 'clade', 'description', 'start', 'stop', 'length']
