from booking.models import Hotel
from rest_framework import serializers
from core.serializers import OwnedByCompanyModelSerializerMixin


class HotelDetailSerializer(
    OwnedByCompanyModelSerializerMixin, 
    serializers.ModelSerializer
    ):

    address = serializers.SerializerMethodField()
    class Meta:
        model = Hotel
        fields = [ 'code', 'name', 'address']


    def get_address(self, instance):
        return dict(
            city=instance.city,
            street=instance.street,
            state=instance.state,
            zip_code=instance.zip_code,
            country=instance.country
        )


class HotelCreateSerializer(
        OwnedByCompanyModelSerializerMixin, 
        serializers.ModelSerializer
    ):
    class Meta:
        model = Hotel
        fields = [
            'name', 
            'city', 
            'street',
            'state',
            'zip_code',
            'country',
        ]