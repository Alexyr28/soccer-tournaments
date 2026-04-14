from django.views.generic import ListView

from django.shortcuts import render

from .models import Tournament
# Create your views here.
class TournamentListView(ListView):
    model = Tournament
    template_name = 'tournaments/tournament_list.html'