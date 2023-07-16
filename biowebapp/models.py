from django.db import models

# models for the database


class PfamDescription(models.Model):
    domain_id = models.CharField(primary_key=True, max_length=255)
    domain_description = models.TextField()

    class Meta:
        db_table = 'pfam_descriptions'


class Organism(models.Model):
    taxa_id = models.CharField(primary_key=True, max_length=255)
    genus = models.CharField(max_length=255)
    species = models.CharField(max_length=255)

    class Meta:
        db_table = 'organisms'


class Protein(models.Model):
    protein_id = models.CharField(primary_key=True, max_length=255)
    taxa = models.ForeignKey(
        Organism, related_name='proteins', on_delete=models.CASCADE)
    clade = models.CharField(max_length=255)
    description = models.TextField()
    start = models.IntegerField()
    stop = models.IntegerField()
    length = models.IntegerField()

    class Meta:
        db_table = 'proteins'


class Domain(models.Model):
    protein = models.ForeignKey(
        Protein, related_name='domains', on_delete=models.CASCADE, db_column='protein_id', default=None)  # Add default value here
    domain = models.ForeignKey(
        PfamDescription, on_delete=models.CASCADE, db_column='domain_id', default=None)  # Add default value here

    class Meta:
        db_table = 'domains'


class Sequence(models.Model):
    protein = models.OneToOneField(
        Protein, related_name='sequence', on_delete=models.CASCADE)
    sequence = models.TextField()

    class Meta:
        db_table = 'sequences'
