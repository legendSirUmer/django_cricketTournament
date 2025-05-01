from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')



def matches(request):
    return render(request, 'matches.html')

def teams(request):
    return render(request, 'team.html')


from django.http import JsonResponse
from .models import LiveScore

def live_score(request, match_id):
    try:
        live_score = LiveScore.objects.get(match_id=match_id)
        data = {
            'match': str(live_score.match),
            'current_score': live_score.current_score,
            'overs': live_score.overs,
            'wickets': live_score.wickets,
            'batsman': live_score.batsman,
            'batsman_score': live_score.batsman_score,
            'runner': live_score.runner,
            'runner_score': live_score.runner_score,
            'bowler': live_score.bowler,
            'last_ball': live_score.last_ball,
            'last_ball_runs': live_score.last_ball_runs,
        }
        return JsonResponse(data)
    except LiveScore.DoesNotExist:
        return JsonResponse({'error': 'Live score not found'}, status=404)