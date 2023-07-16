from django.shortcuts import render
from .models import *

# Create your views here.

# similar code to the one in the class. Modified to fit the project

def index(request):
    organisms = Organism.objects.all()
    return render(request, 'biowebapp/index.html', {'organisms': organisms})

def genus_species(request):
    organisms = Organism.objects.all()
    return render(request, 'biowebapp/genus_species.html', {'organisms': organisms})


def organism(request, pk):
    organism = Organism.objects.get(pk=pk)
    return render(request, 'biowebapp/organism.html', {'organism': organism})
