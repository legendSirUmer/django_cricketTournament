from django.shortcuts import render
from .models import Player, Match, MatchDetails, LiveScore, Score, Team
import datetime
# Create your views here.
def index(request):
    matches = Match.objects.all()
    next_match = matches.filter(date__gt=datetime.date.today()).order_by('date').first()
    current_match = matches.filter(date=datetime.date.today()).first()
    current_live_score = LiveScore.objects.filter(match=current_match).first() 
    # print( "current liveScore id" , current_live_score.id)
    # print( "current match Team 1" , current_match.team1.name)
    # print( "current match Team 2" , current_match.team2.name)
    
    previous_matches = matches.filter(date__lt=datetime.date.today()).order_by('-date')[:5]
    return render(request, 'index.html', {'matches': matches, 'next_match': next_match, 'previous_matches': previous_matches, 'current_match': current_live_score})



def contact(request):
    return render(request, 'contact.html')





def matches(request):
    matches = Match.objects.all()
    return render(request, 'matches.html',{'matches': matches})


from django.shortcuts import render, get_object_or_404
from .models import Match, MatchDetails, Score

from .models import Match, MatchDetails, Score, LiveScoreHistory

def match_details(request):
    if request.method == "POST":
        matches = Match.objects.all()
        match_id = request.POST.get('match_id')
        match = get_object_or_404(Match, id=match_id)
        match_details = MatchDetails.objects.filter(match=match).first()
        scores = Score.objects.filter(match=match)
        live_score_history = LiveScoreHistory.objects.filter(match=match).order_by('-timestamp')
        

        context = {
            'match': match,
            'match_details': match_details,
            'scores': scores,
            'matches': matches,
            'live_score_history': live_score_history,
        }
        return render(request, 'matches.html', context)
    else:
        return render(request, 'matches.html', {'matches': Match.objects.all()})



def teams(request):

    teams = Team.objects.all()
    context = {
        'teams': teams,
    }
    
    return render(request, 'team.html',context)


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
            'batsman': live_score.batsman.name,
            'batsman_score': live_score.batsman_score,
            'runner': live_score.runner.name,
            'runner_score': live_score.runner_score,
            'bowler': live_score.bowler.name,
            'last_ball_runs': live_score.last_ball_runs,
        }
        return JsonResponse(data)
    except LiveScore.DoesNotExist:
        return JsonResponse({'error': 'Live score not found'}, status=404)
    











from django.shortcuts import redirect
from .models import Messages
from django.contrib import messages as flash_messages  # For success/error messages

def contact(request):
    if request.method == "POST":
        first_name = request.POST.get('c_fname')
        last_name = request.POST.get('c_lname')
        email = request.POST.get('c_email')
        subject = request.POST.get('c_subject')
        message = request.POST.get('c_message')

        # Save the message to the database
        Messages.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            subject=subject,
            message=message
        )

        # Add a success message
        flash_messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')  # Redirect to the contact page after submission

    return render(request, 'contact.html')