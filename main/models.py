from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    team = models.CharField(max_length=100)
    enrollment = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Match(models.Model):
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.team1} vs {self.team2}"
    



class Score(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    team = models.CharField(max_length=100)
    runs = models.IntegerField()
    wickets = models.IntegerField()
    overs = models.FloatField()

    def __str__(self):
        return f"{self.match} - {self.team}"
    

class Team(models.Model):
    name = models.CharField(max_length=100)
    players = models.ManyToManyField(Player, related_name='teams')

    def __str__(self):
        return self.name