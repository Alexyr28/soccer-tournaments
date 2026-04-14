from django.db import models

# Create your models here.
class Tournament(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return self.name
class Team(models.Model):
    name = models.CharField(max_length=100)
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Game(models.Model):
    local_team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='local_games')
    visitor_team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='visitor_games')
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.local_team} vs {self.visitor_team}"
class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class GameEvent(models.Model):
    typeEvent = models.CharField(max_length=50)
    minute = models.IntegerField()
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    player = models.ForeignKey('Player', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.typeEvent} - {self.minute}"