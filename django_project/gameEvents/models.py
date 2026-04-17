from django.db import models

class Game(models.Model):
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.id}"  


class GameEvent(models.Model):
    typeEvent = models.CharField(max_length=50)
    minute = models.IntegerField()
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    player = models.ForeignKey('player.Player', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.typeEvent} - {self.minute}"