# Generated by Django 3.1.6 on 2021-02-18 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokemon_element', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PokemonSpecies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('evolution_level', models.PositiveIntegerField(default=0)),
                ('new_evolution', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='identity.pokemonspecies')),
                ('pokemon_types', models.ManyToManyField(to='identity.PokemonType')),
            ],
        ),
        migrations.CreateModel(
            name='Pokemons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('level', models.PositiveIntegerField(default=0)),
                ('species', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='identity.pokemonspecies')),
            ],
        ),
    ]