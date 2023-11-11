from django.db import models


class Match(models.Model):
    stadium = models.ForeignKey('stadiums.Stadium', on_delete=models.CASCADE)
    date_and_time = models.DateTimeField()

    class Meta:
        unique_together = ('stadium', 'date_and_time')
