from django.db import models

# Create your models here.
class Season(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)

class Division(models.Model):
    season = models.ForeignKey(
        Season,
        related_name='divisions',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    leagueId = models.CharField(max_length=100)


    def __str__(self):
        return self.name
