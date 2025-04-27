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


