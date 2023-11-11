from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Ticket
from .serializers import TicketPurchaseSerializer
from .utils.buy_ticket import TicketingAPIClient
from .exceptions import SeatNotAvailableError, PaymentFailedError
from seats.models import Seat


class TicketingAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Assuming authentication is used to identify the user
        user = request.user

        # Validate incoming data using the new serializer
        serializer = TicketPurchaseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        match_id = serializer.validated_data['match_id']
        seat_ids = serializer.validated_data['seat_ids']

        try:
            # Perform ticket purchase logic using the TicketingAPIClient
            result = TicketingAPIClient.buy_tickets(user, Seat, Ticket, match_id, seat_ids)
            return Response(result, status=status.HTTP_200_OK)
        except SeatNotAvailableError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except PaymentFailedError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
