from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from tournaments.models import GameEvent, Player
from .serializers import GameEventSerializer, PlayerSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class GameEventViewSet(viewsets.ModelViewSet):
    queryset = GameEvent.objects.all()
    serializer_class = GameEventSerializer