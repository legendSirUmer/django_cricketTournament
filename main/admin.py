from django.contrib import admin
from .models import LiveScoreHistory

# Register your models here.
admin.site.site_header = "Cricket Tournament Admin"


admin.site.site_title = "Cricket Tournament Admin Portal"

admin.site.index_title = "Welcome to the Cricket Tournament Admin Portal"

from .models import Player, Match, MatchDetails, LiveScore, Score, Team

admin.site.register(Player)
admin.site.register(Match)
admin.site.register(MatchDetails)

admin.site.register(Score)
admin.site.register(Team)
admin.site.register(LiveScoreHistory)


@admin.register(LiveScore)
class LiveScoreAdmin(admin.ModelAdmin):
    list_display = ('match', 'current_score', 'overs', 'wickets', 'batsman', 'batsman_score', 'runner', 'runner_score', 'bowler', 'last_ball_runs', 'ball_type')
    fields = ('match', 'current_score', 'overs', 'wickets', 'batsman', 'batsman_score', 'runner', 'runner_score', 'bowler', 'last_ball_runs', 'ball_type')


from .models import Messages

@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'subject', 'timestamp')
    search_fields = ('first_name', 'last_name', 'email', 'subject')