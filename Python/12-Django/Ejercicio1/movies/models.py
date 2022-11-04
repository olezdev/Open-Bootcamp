from django.db import models

class Director(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null= True, blank = True)
    nationality = models.CharField(max_length=50)
    # filmography = models.ManyToManyField(Movie)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Genre(models.Model):
    name = models.CharField(max_length=64, help_text="Ingrese el nombre de género")

    def __str__(self):
        return self.name

class Movie(models.Model):
    director = models.ForeignKey('Director', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    synopsis = models.TextField()
    duration = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

