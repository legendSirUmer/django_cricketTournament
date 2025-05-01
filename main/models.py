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
    
class MatchDetails(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    toss_winner = models.CharField(max_length=100)
    toss_decision = models.CharField(max_length=100)
    match_winner = models.CharField(max_length=100)
    player_of_the_match = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.match} - {self.player_of_the_match}"
    
class LiveScore(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    current_score = models.CharField(max_length=100)
    overs = models.FloatField()
    wickets = models.IntegerField()
    batsman = models.CharField(max_length=100)  # Name of the batsman
    batsman_score = models.IntegerField()  # Score of the batsman
    runner = models.CharField(max_length=100)  # Name of the runner
    runner_score = models.IntegerField()  # Score of the runner
    bowler = models.CharField(max_length=100)  # Name of the bowler
    last_ball = models.CharField(max_length=100)  # Description of the last ball
    last_ball_runs = models.IntegerField()  # Runs scored on the last ball
    

    def __str__(self):
        return f"{self.match} - {self.current_score}"

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



class NextMatch(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    next_match = models.ForeignKey(Match, related_name='next_matches', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.match} - {self.next_match}"