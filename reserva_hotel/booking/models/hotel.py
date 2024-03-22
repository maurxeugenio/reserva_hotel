from django.db import models
from core.models import OwnedByCompany
from decimal import Decimal


class Hotel(OwnedByCompany):
    name = models.CharField(
        max_length=200,
        default=""
    )
    street = models.CharField(
        max_length=255, 
        default=""
    )
    city = models.CharField(
        max_length=255, 
        default=""
    )
    state = models.CharField(
        max_length=255, 
        default=""
    )
    zip_code = models.CharField(
        max_length=20, 
        default=""
    )
    country = models.CharField(
        max_length=255, 
        default=""
    ) 

    def __str__(self) -> str:
        return self.name
    

class Room(OwnedByCompany):
    class Types(models.TextChoices):
        STANDARD = 'standard', 'Standard Room'
        DOUBLE = 'double', 'Double Room'
        TWIN = 'twin', 'Twin Room'
        SINGLE = 'single', 'Single Room'
        SUITE = 'suite', 'Suite'
        DELUXE = 'deluxe', 'Deluxe Room'
        FAMILY = 'family', 'Family Room'
        CONNECTING = 'connecting', 'Connecting Rooms'
        ADJOINING = 'adjoining', 'Adjoining Rooms'
        ACCESSIBLE = 'accessible', 'Accessible Room'
        JUNIOR_SUITE = 'junior_suite', 'Junior Suite'
        PRESIDENTIAL_SUITE = 'presidential_suite', 'Presidential Suite'
    
    class Status(models.TextChoices):
        AVAILABLE = 'available', 'Available'
        OCCUPIED = 'occuped', 'Occupied'
        UNDER_MAINTENANCE = 'maintenance', 'Under Maintenance'

    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        related_name='rooms'
    )
    room_type = models.CharField(
        max_length=200, 
        default="", 
        choices=Types.choices
    )
    status = models.CharField(
        max_length=100, 
        default="", 
        choices=Status.choices
    )
    capacity = models.IntegerField(default=1)
    number = models.IntegerField(blank=True, default=1)
    price_per_nigth = models.DecimalField(
        default=Decimal("0.00"),
        max_digits=10,
        decimal_places=2
    )

    def __str__(self) -> str:
        return f'Room #{self.number}'