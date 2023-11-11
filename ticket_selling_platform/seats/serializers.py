from rest_framework import serializers
from .models import Match, Seat


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'

    def validate(self, data):
        row = data['row']
        column = data['column']
        match = data['match']

        # Check if the seat is within the range of the stadium's rows and columns
        stadium = match.stadium
        if row < 1 or row > stadium.rows or column < 1 or column > stadium.columns:
            raise serializers.ValidationError("Seat position is out of range.")


        return data
