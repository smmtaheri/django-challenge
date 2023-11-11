from rest_framework import serializers
from .models import Stadium


class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = '__all__'

    def validate(self, data):
        # Check if the capacity is a multiple of rows and columns
        if data['capacity'] % (data['rows'] * data['columns']) != 0:
            raise serializers.ValidationError("Capacity must be a multiple of rows and columns.",
                                              code='invalid_capacity')

        return data
