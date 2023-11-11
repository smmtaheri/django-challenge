from django.db import models
from matches.models import Match


class Seat(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    row = models.PositiveIntegerField()
    column = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    status = models.BooleanField(default=True)  # This is for availability of a seat.

    # True means available and False means not available. (Sold or anything else)

    class Meta:
        unique_together = ['match', 'row', 'column']

    def save(self, *args, **kwargs):
        # Check if the seat is within the specified range of rows and columns
        if self.row > self.match.stadium.rows or self.column > self.match.stadium.columns:
            raise ValueError("Seat position is outside the specified range.")

        # Check if the seat is not already defined for this match
        if Seat.objects.filter(match=self.match, row=self.row, column=self.column).exists():
            raise ValueError("Seat already defined for this position in the match.")

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Seat {self.row}-{self.column} for {self.match}"
