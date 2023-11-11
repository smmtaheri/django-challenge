from django.urls import path
from .views import TicketingAPI

urlpatterns = [
    path('buy/', TicketingAPI.as_view(), name='buy_ticket'),
]
