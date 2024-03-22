from django.contrib import admin
from .models import Hotel, Room, Booking

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = [
        '__str__', 
        'company',
        'hotel',
        'status',
        'capacity', 
        'price_per_nigth', 
    ]

    list_filter = [
        'company'
    ]


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'number_of_rooms']


    def number_of_rooms(self, object):
        return object.rooms.count()
    
    

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = [
        'code', 
        'user', 
        'room', 
        'check_in', 
        'check_out', 
        'quantity_people',
        'quantity_days',
        'total_price'
    ]

