from booking.models import Booking
from booking.services import BookingService
from core.models import User


class BookingFacade:
    @staticmethod
    def process_booking(booking: Booking, user: User):
        booking = BookingService.set_user_and_company(
            booking=booking,
            room=booking.room,
            user=user
        )
        booking = BookingService.calculate_quantity_days(
            booking=booking
        )
        
        BookingService.calculate_total_price(booking=booking)
    
        BookingService.send_confirmation_email(
            user=user, 
            room=booking.room
        )