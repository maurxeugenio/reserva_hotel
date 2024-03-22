from rest_framework import serializers
from booking.models import Room, Booking
from django.utils import timezone
from datetime import datetime
from booking.facades import BookingFacade
from .hotel import HotelDetailSerializer


class BookingDetailSerializer(serializers.ModelSerializer):
    code = serializers.CharField()
    check_in = serializers.DateField(format='%Y-%m-%d')
    check_out = serializers.DateField(format='%Y-%m-%d')
    quantity_people = serializers.IntegerField()
    room = serializers.SlugRelatedField(
        queryset=Room.objects.all(),
        slug_field='code'
    )
    hotel = HotelDetailSerializer(source='room.hotel')

    class Meta:
        model = Booking
        fields = [
            'code', 
            'check_in', 
            'check_out', 
            'quantity_people', 
            'room',
            'hotel'
        ]


class BookingCreateSerializer(serializers.ModelSerializer):
    check_in = serializers.DateField(format='%Y-%m-%d')
    check_out = serializers.DateField(format='%Y-%m-%d')
    quantity_people = serializers.IntegerField()
    room = serializers.SlugRelatedField(
        queryset=Room.objects.all(),
        slug_field='code'
    )

    class Meta:
        model = Booking
        fields = ['check_in', 'check_out', 'quantity_people', 'room']

    def validate_check_in(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Check-in date must be in the future.")
        return value

    def validate_check_out(self, value):
        check_in_str = self.initial_data.get('check_in')
        check_in_date = datetime.strptime(check_in_str, '%Y-%m-%d')

        if value <= check_in_date.date():
            raise serializers.ValidationError("check_out date must be after check-in date.")
        return value

    def validate_quantity_people(self, value):
        if value < 0:
            raise serializers.ValidationError("Quantity of people cannot be negative.")
        return value

    def validate_room(self, value):
        check_in = self.initial_data.get('check_in')
        check_out = self.initial_data.get('check_out')
        
        # Check if the room is available for the given check_in and checkout dates
        bookings_overlap = Booking.objects.filter(
            room=value,
            check_in__lt=check_out,
            check_out__gt=check_in
        ).exists()
        
        if bookings_overlap:
            raise serializers.ValidationError("This room is not available for the selected dates.")
                
        return value
    

    def create(self, validated_data):
        instance = super().create(validated_data)
        user = self.context.get('user')
        BookingFacade.process_booking(
            booking=instance, 
            user=user
        )

        return instance