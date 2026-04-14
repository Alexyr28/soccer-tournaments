from rest_framework import serializers
from tournaments.models import GameEvent, Player




class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class GameEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameEvent
        fields = '__all__'