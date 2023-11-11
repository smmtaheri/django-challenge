from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .models import Seat
from .serializers import SeatSerializer


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]  # Only admins can handle seat model

    def create(self, request, *args, **kwargs):
        row = request.data.get('row')
        column = request.data.get('column')
        match = request.data.get('match')

        # Check for an existing seat with the same row, column, and match
        existing_seat = Seat.objects.filter(row=row, column=column, match=match).exists()
        if existing_seat:
            return Response({"detail": "Seat already exists at this position."}, status=status.HTTP_400_BAD_REQUEST)

        # Create a temporary serializer instance for validation
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return super().create(request, *args, **kwargs)
