from django.contrib import admin

from . import models
# Register your models here.

admin.site.site_header = 'Pokemon Administration'
admin.site.site_title = 'Pokemon Administration'
admin.site.index_title = 'Pokemon Administration'

admin.site.register(models.PokemonType)


class PokemonSpeciesAdmin(admin.ModelAdmin):
    list_display = ['name', 'show_types', 'evolution_level', 'new_evolution',]
    filter_horizontal = ['pokemon_type']

admin.site.register(models.PokemonSpecies, PokemonSpeciesAdmin)


class PokemonsAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'level', 'trainer']

admin.site.register(models.Pokemons, PokemonsAdmin)