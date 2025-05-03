from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import LiveScore, LiveScoreHistory

@receiver(post_save, sender=LiveScore)
def save_live_score_history(sender, instance, **kwargs):
    LiveScoreHistory.objects.create(
        match=instance.match,
        current_score=instance.current_score,
        overs=instance.overs,
        wickets=instance.wickets,
        batsman=instance.batsman,
        batsman_score=instance.batsman_score,
        runner=instance.runner,
        runner_score=instance.runner_score,
        bowler=instance.bowler,
        last_ball_runs=instance.last_ball_runs,
        ball_type=instance.ball_type,
    )