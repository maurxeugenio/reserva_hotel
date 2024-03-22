from rest_framework import serializers
from booking.models import Room, Hotel
from core.serializers import (
    OwnedByCompanyModelSerializerMixin, OwnedByCompanyRelatedField
)


class RoomDetailSerializer(
    OwnedByCompanyModelSerializerMixin, 
    serializers.ModelSerializer
):  
    hotel = serializers.SlugRelatedField(
        slug_field='code', 
        queryset=Hotel.objects.all()
    )
    
    class Meta:
        fields = [
            'code',
            'hotel',
            'status',
            'capacity',
            'room_type',
            'number',
            'price_per_nigth'
        ]
        model = Room


class RoomCreateSerializer(
    OwnedByCompanyModelSerializerMixin, 
    serializers.ModelSerializer
):
    hotel = OwnedByCompanyRelatedField(queryset=Hotel.objects.all())
    class Meta:
        fields = [
            'hotel',
            'status',
            'capacity',
            'room_type',
            'number',
            'price_per_nigth'
        ]
        model = Room