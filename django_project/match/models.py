from django.db import models

# Create your models here.
class Match(models.Model):
    number=models.IntegerField()
    start_date=models.DateField()
    
    def __str__(self):
        return f"Match {self.number} starting on {self.start_date}"
