from django.db import models


class Animal(models.Model):
    species = models.CharField(max_length=40)
    says = models.CharField(max_length=40)

    def __str__(self):
        return self.species
