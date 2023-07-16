from django.urls import path, include
from . import views
from .api import *

# url patterns for the app
urlpatterns = [
    path('', views.index, name='index'),
    path('genus_species', views.genus_species, name='genus_species'),
    path('organism/<int:pk>', views.organism, name='organism'),
    path('api/protein/<str:protein_id>/',
         ProteinAPIView.as_view(), name='protein'),
    path('api/pfam/<str:pfam_id>/', PfamAPIView.as_view(), name='pfam'),
    path('api/proteins/<str:taxa_id>/',
         ProteinsByTaxaIdView.as_view(), name='proteins_by_taxa_id'),
    path('api/coverage/<str:protein_id>', CoverageAPIView.as_view()),
    path('api/pfams/<str:taxa_id>', PfamsByTaxaIdView.as_view()),
]
