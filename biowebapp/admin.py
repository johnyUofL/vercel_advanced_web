from django.contrib import admin
from .models import PfamDescription, Organism, Protein, Domain, Sequence


class PfamDescriptionAdmin(admin.ModelAdmin):
    list_display = ('domain_id', 'domain_description',)
    search_fields = ('domain_id',)


class OrganismAdmin(admin.ModelAdmin):
    list_display = ('taxa_id', 'genus', 'species',)
    search_fields = ('taxa_id', 'genus', 'species',)


class ProteinAdmin(admin.ModelAdmin):
    list_display = ('protein_id', 'taxa', 'clade',
                    'description', 'start', 'stop', 'length',)
    search_fields = ('protein_id', 'clade',)


class DomainAdmin(admin.ModelAdmin):
    list_display = ('protein', 'domain',)
    search_fields = ('protein__protein_id', 'domain__domain_id',)


class SequenceAdmin(admin.ModelAdmin):
    list_display = ('protein', 'sequence',)
    search_fields = ('protein__protein_id',)


admin.site.register(PfamDescription, PfamDescriptionAdmin)
admin.site.register(Organism, OrganismAdmin)
admin.site.register(Protein, ProteinAdmin)
admin.site.register(Domain, DomainAdmin)
admin.site.register(Sequence, SequenceAdmin)
