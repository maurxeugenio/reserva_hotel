from core.models import User
from celery import shared_task
from booking.models import Room
from datetime import date


@shared_task
def send_email_confirmation_booking(user_id: int, room_id: int):
    from booking.services import EmailService
    user = User.objects.get(pk=user_id)
    room = Room.objects.get(pk=room_id)
    
    EmailService.send_email(
        subject='Your Reservation has been confirmed',
        message=(
            f"Hello {user.get_full_name()},\n"
            f"Your reservation at the {room.hotel} hotel,\n"
            f"Room number {room.number},\n"
            f"has just been confirmed." 
        ),
        recipient_list=[user.email]
    )

@shared_task
def send_email_cancelation_booking(user_id: int, room_id: int):
    from booking.services import EmailService
    user = User.objects.get(pk=user_id)
    room = Room.objects.get(pk=room_id)
    
    EmailService.send_email(
        subject='Your Reservation has been canceled',
        message=(
            f"Hello {user.get_full_name()},\n"
            f"Your reservation at the {room.hotel.name},\n"
            f"Room number {room.number},\n"
            f"has just been confirmed." 
        ),
        recipient_list=[user.email]
    ) 


@shared_task
def verify_rooms():
    today = date.today()

    rooms = Room.objects.filter(
        status=Room.Status.OCCUPIED,
        booking__check_out__lt=today
    )
    
    rooms.update(status=Room.Status.AVAILABLE)
