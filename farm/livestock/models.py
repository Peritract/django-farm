from django.db import models

# Create your models here.

class Species(models.Model):

    name = models.CharField(max_length=100)

    def __repr__(self):
        return "Species: " + self.name

    def __str__(self):
        return "Species: " + self.name

class Animal(models.Model):

    name = models.CharField(max_length=15)
    species = models.ForeignKey(Species,
                                on_delete=models.SET_NULL,
                                null=True)
    age = models.IntegerField()
    hopes_and_dreams = models.CharField(max_length=1000)

    def __repr__(self):
        return f"{self.name}, a {self.species.name}"
    
    def __str__(self):
        return f"{self.name}, a {self.species.name}"

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "species": self.species.name,
            "hopes_and_dreams": self.hopes_and_dreams
        }