from django.db import models
from core.models import OwnedByCompany
from decimal import Decimal


class Booking(OwnedByCompany):
    user = models.ForeignKey(
        'core.User',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    room = models.ForeignKey(
        'booking.Room',
        on_delete=models.CASCADE
    )
    check_in = models.DateField()
    check_out = models.DateField()
    quantity_people = models.IntegerField(blank=True, default=1)
    quantity_days = models.IntegerField(blank=True, default=0)
    total_price = models.DecimalField(
        default=Decimal('0.00'),
        decimal_places=2,
        max_digits=10
    )