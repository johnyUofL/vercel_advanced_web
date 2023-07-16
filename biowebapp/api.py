from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import *

# Implementation of API views
# APIView for protein


class ProteinAPIView(APIView):
    def get(self, request, protein_id):
        # We use a try/except block to catch the case where the protein does not exist
        try:
            protein = Protein.objects.get(protein_id=protein_id)
            serializer = ProteinSerializer(protein)
            return Response(serializer.data)
        except Protein.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
# returning 201 status code if the protein is created successfully and 400 if not

    def post(self, request):
        serializer = ProteinCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# APIView for Pfam


class PfamAPIView(APIView):
    def get(self, request, pfam_id):
        # We use a try/except block to catch the case where the Pfam does not exist
        try:
            pfam_description = PfamDescription.objects.get(pk=pfam_id)
            serializer = PfamDescriptionSerializer(pfam_description)
            return Response(serializer.data)
        except PfamDescription.DoesNotExist:
            # return 404 status code if the Pfam does not exist
            return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

# APIView for protein list filtered by taxa_id


class ProteinsByTaxaIdView(APIView):
    def get(self, request, taxa_id):
        proteins = Protein.objects.filter(taxa__taxa_id=taxa_id)
        serializer = ProteinListSerializer(proteins, many=True)
        return Response(serializer.data)

# APIView for coverage


class CoverageAPIView(APIView):
    def get(self, request, protein_id):
        # use a try/except block to catch the case where the an object does not exist
        try:
            protein = Protein.objects.get(protein_id=protein_id)

    # use 'start' and 'stop' to calculate the domain length
            domain_length = protein.stop - protein.start

    # Calculating the coverage using domain_length and protein.length
            coverage = domain_length / protein.length if protein.length else 0

            return Response({'coverage': coverage})

        except Protein.DoesNotExist:
            # return 404 status code if the protein does not exist
            return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)


class PfamsByTaxaIdView(APIView):
    def get(self, request, taxa_id):
        proteins = Protein.objects.filter(taxa__taxa_id=taxa_id)
        domains = Domain.objects.filter(protein__in=proteins).exclude(
            domain__domain_id__isnull=True, domain__domain_description__isnull=True)
        serializer = TaxaPfamSerializer(domains, many=True)
        return Response(serializer.data)
