from django.db import models
from matches.models import Match
from seats.models import Seat


class Ticket(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.match} - Seat {self.seat.row}{self.seat.column}"
