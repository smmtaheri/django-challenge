from django.db import transaction

from .bank_gateway import BankGateway
from ..exceptions import SeatNotAvailableError, PaymentFailedError


class TicketingAPIClient:
    @staticmethod
    @transaction.atomic
    def buy_tickets(user: 'User', seat: 'Seat', ticket: 'Ticket', match_id: int, seat_ids: list[int]) -> dict:
        """
        Buy tickets for the specified seats in a match.

        :param user: The user for whom the tickets are being purchased.
        :param seat: The Seat model.
        :param ticket: The Ticket model.
        :param match_id: The ID of the match.
        :param seat_ids: A list of seat IDs to purchase.

        :return: A dictionary containing the result of the transaction.
        """

        # Lock all selected seats for the transaction
        seats = seat.objects.select_for_update().filter(id__in=seat_ids, match__id=match_id, status=True)

        # Check if all selected seats are available
        if len(seats) != len(seat_ids):
            raise SeatNotAvailableError("Some selected seats are not available.")

        # Calculate the total price for all selected seats
        total_price = sum(seat.price for seat in seats)

        # Call an external payment gateway
        payment_success, payment_message = BankGateway.process_payment()

        if payment_success:
            # Simulate a successful payment

            # Create tickets for the user
            ticket_objs = [ticket.objects.create(user=user, seat=seat, match=seat.match) for seat in seats]

            tickets = [
                {
                    "id": t.id,
                    "seat_id": t.seat_id,
                }
                for t in ticket_objs
            ]

            # Update the status of all selected seats to False (reserved)
            seats.update(status=False)

            return {
                "detail": "Tickets purchased successfully.",
                "tickets": tickets,
                "match_id": match_id,
                "total_price": total_price
            }
        else:
            # Simulate a fail payment

            # Rollback the transaction (release the lock)
            raise PaymentFailedError("Payment failed. Seats are not reserved.")
