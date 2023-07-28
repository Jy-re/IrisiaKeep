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
    world_name = models.CharField(max_length=225)
    overview = models.TextField()
    geography = models.TextField()
    culture_society = models.TextField()
    history = models.TextField()
    magic_tech = models.TextField()
    politics = models.TextField()
    economy = models.TextField()
    creatures = models.TextField()
    language = models.TextField()
    arts = models.TextField()
    miscellaneous = models.TextField()
    image = models.FileField(blank=True)

class Book(models.Model):
    plot = models.TextField()
    author = models.CharField(max_length=225)
    date_started = models.DateField()
    date_ended = models.DateField()
    lore = models.ForeignKey(Lore, on_delete=models.CASCADE)
    characters = models.ForeignKey(Character, on_delete=models.CASCADE)
    image = models.FileField(blank=True)

class Post(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField()
    image = models.FileField(blank=True)