from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=100)
    enrollment = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Team(models.Model):
    name = models.CharField(max_length=100)
    players = models.ManyToManyField(Player, related_name='teams')

    def __str__(self):
        return self.name

class Match(models.Model):

    team1 = models.ForeignKey(Team, related_name='team1', on_delete=models.CASCADE) 
    team2 = models.ForeignKey(Team, related_name='team2', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.team1} vs {self.team2}"
    
class LiveScore(models.Model):
    BALL_TYPES = [
        ('normal', 'Normal Ball'),
        ('white', 'White Ball'),
        ('no_ball', 'No Ball'),
    ]

    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    current_score = models.CharField(max_length=100)  # Format: "Runs/Wickets"
    overs = models.FloatField(default=-0.1)  # Current overs
    wickets = models.IntegerField()  # Total wickets
    batsman = models.ForeignKey(Player,related_name='batsman',on_delete=models.CASCADE)  # Name of the batsman
    batsman_score = models.IntegerField(default=0)  # Score of the batsman
    runner = models.ForeignKey(Player,related_name='runner',on_delete=models.CASCADE)   # Name of the runner
    runner_score = models.IntegerField(default=0)  # Score of the runner
    bowler = models.ForeignKey(Player,related_name='bowler',on_delete=models.CASCADE) #nAme of the bowler
    last_ball_runs = models.IntegerField(default=0)  # Runs scored on the last ball
    ball_type = models.CharField(max_length=10, choices=BALL_TYPES, default='normal')  # Type of ball

    def save(self, *args, **kwargs):
        # Check if the batsman or runner name has changed
        if self.pk:  # Check if the object already exists in the database
            previous_instance = LiveScore.objects.get(pk=self.pk)
            if self.batsman != previous_instance.batsman or self.runner != previous_instance.runner:
                # Increment the wicket count if batsman or runner has changed
                self.wickets += 1

        # Extract current runs and wickets from the current_score
        if self.current_score:
            runs, wickets = map(int, self.current_score.split('/'))
        else:
            runs, wickets = 0, 0

        # Update the total score
        runs += self.last_ball_runs

        # Update the batsman's score
        self.batsman_score += self.last_ball_runs

        # Handle ball type logic
        if self.ball_type == 'normal':
            # Increment overs for a normal ball
            overs_int = int(self.overs)  # Integer part of overs
            overs_decimal = self.overs - overs_int  # Decimal part of overs
            overs_decimal += 0.1  # Increment by 0.1 for each ball
            if overs_decimal >= 0.6:  # Carry over to the next over
                overs_decimal = 0.0
                overs_int += 1
            self.overs = overs_int + overs_decimal
        elif self.ball_type == 'white':
            # White ball: Add 1 run but do not increment overs
            runs += 1
        elif self.ball_type == 'no_ball':
            # No ball: Add 1 run but do not increment overs
            runs += 1

        # Update the runner's score if the last ball run is 1 or 3
        if self.last_ball_runs in [1, 3]:
            self.batsman, self.runner = self.runner, self.batsman  # Switch batsman and runner
            self.batsman_score, self.runner_score = self.runner_score, self.batsman_score

        # Update the current_score field
        self.current_score = f"{runs}/{self.wickets}"

        # Call the parent save method
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.match} - {self.current_score}"

class Score(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    runs = models.IntegerField()
    wickets = models.IntegerField()
    overs = models.FloatField()

    def __str__(self):
        return f"{self.match} - {self.team}"
    


class MatchDetails(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    Score1 = models.ForeignKey(Score, related_name='score1', on_delete=models.CASCADE)
    Score2 = models.ForeignKey(Score, related_name='score2', on_delete=models.CASCADE)
    toss_winner = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='toss_winner')
    toss_decision = models.CharField(max_length=100 , choices=[('bat', 'Bat'), ('bowl', 'Bowl')])
    match_winner = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='match_winner')
    player_of_the_match = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.match} - {self.player_of_the_match}"
    





class LiveScoreHistory(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    current_score = models.CharField(max_length=100)  # Format: "Runs/Wickets"
    overs = models.FloatField()  # Current overs
    wickets = models.IntegerField()  # Total wickets
    batsman = models.CharField(max_length=100)  # Name of the batsman
    batsman_score = models.IntegerField(default=0)  # Score of the batsman
    runner = models.CharField(max_length=100)  # Name of the runner
    runner_score = models.IntegerField(default=0)  # Score of the runner
    bowler = models.CharField(max_length=100)  # Name of the bowler
    last_ball_runs = models.IntegerField(default=0)  # Runs scored on the last ball
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp of the change
    ball_type = models.CharField(max_length=10, choices=LiveScore.BALL_TYPES, default='normal')  # Type of ball

    def __str__(self):
        return f"{self.match} - {self.current_score} at {self.timestamp}"
    


class Messages(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"













    