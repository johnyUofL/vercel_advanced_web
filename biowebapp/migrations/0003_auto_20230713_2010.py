# Generated by Django 3.0.3 on 2023-07-13 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biowebapp', '0002_auto_20230713_1943'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sequence',
            old_name='protein',
            new_name='protein_id',
        ),
        migrations.AlterField(
            model_name='domain',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sequence',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]