from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    personality = models.TextField()
    background = models.TextField()
    goals = models.TextField()
    strengths = models.TextField()
    weakness = models.TextField()
    skills = models.TextField()
    hobbies = models.TextField()
    backstory = models.TextField()
    image = models.FileField(blank=True)

class Lore(models.Model):
    worldname = models.CharField(max_length=225)
    overview = models.TextField()
    geography = models.TextField()
    culturesociety = models.TextField()
    history = models.TextField()
    magictech = models.TextField()
    politics = models.TextField()
    economy = models.TextField()
    creatures = models.TextField()
    language = models.TextField()
    arts = models.TextField()
    miscellaneous = models.TextField()
    image = models.FileField(blank=True)

class Book(models.Model):
    title = models.CharField(max_length=225, null=True)
    plot = models.TextField()
    author = models.CharField(max_length=225)
    datestart = models.DateField()
    lore = models.ForeignKey(Lore, on_delete=models.CASCADE)
    characters = models.ManyToManyField(Character)  # Update to ManyToManyField
    image = models.FileField(blank=True)

class Post(models.Model):
    title = models.CharField(max_length=225, null=True)
    content = models.TextField()
    image = models.FileField(blank=True)