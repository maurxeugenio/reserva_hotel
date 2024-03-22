from booking.models import Booking, Room
from core.models import User
from booking.tasks import send_email_confirmation_booking


class BookingService:
    @staticmethod
    def set_user_and_company(
        booking: Booking, 
        room: Room, 
        user: User
    ) -> Booking:
        booking.user = user
        booking.company = room.company
        booking.save()

        return booking

    @staticmethod
    def calculate_quantity_days(booking: Booking) -> Booking:
        quantity_days = booking.check_out - booking.check_in
        booking.quantity_days = quantity_days.days
        booking.save()

        return booking

    @staticmethod
    def calculate_total_price(booking: Booking) -> Booking:
        price_per_nigth = booking.room.price_per_nigth
        total_price = price_per_nigth * booking.quantity_days
        booking.total_price = total_price
        booking.save()
        
        return booking
    
    @staticmethod
    def send_confirmation_email(user: User, room: Room):
        send_email_confirmation_booking.apply_async(args=[user.id, room.id])