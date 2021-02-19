from django.db import models
from django.db.models import Count
from django.contrib.auth.models import User

# Create your models here.
class PokemonType(models.Model):
    pokemon_element = models.CharField(
        max_length=200,
        verbose_name='Name'
    )

    def __str__(self):
        return self.pokemon_element


class PokemonSpecies(models.Model):
    name = models.CharField(max_length=200)
    evolution_level = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    new_evolution = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    pokemon_type = models.ManyToManyField(PokemonType)

    class Meta:
        verbose_name_plural = 'Pokemon species'

    def show_types(self):
        return ",\n".join([str(pokemon_type) 
                          for pokemon_type in self.pokemon_type.all()
                        ])

    def __str__(self):
        return self.name


class Pokemons(models.Model):
    name = models.CharField(max_length=200)
    species = models.ForeignKey(
        PokemonSpecies,
        on_delete=models.CASCADE,
        null=True
    )
    level = models.PositiveIntegerField(default=1)
    trainer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=User
    )

    class Meta:
        verbose_name_plural = 'Pokemons'

    def save(self,*args,**kwargs):
        if self.level >= self.species.evolution_level:
            self.species = self.species.new_evolution
                
        return super().save()
    
    def __str__(self):
        return '{} {}'.format(self.name, self.species)