from rest_framework import serializers


class TicketPurchaseSerializer(serializers.Serializer):
    match_id = serializers.IntegerField()
    seat_ids = serializers.ListField(child=serializers.IntegerField(), required=True)
