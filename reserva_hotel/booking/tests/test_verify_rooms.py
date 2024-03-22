from django.test import TestCase
from booking.tasks import verify_rooms
from booking.models import Room, Booking, Hotel
from datetime import datetime
from freezegun import freeze_time


class VerifyRoomTests(TestCase):
    def setUp(self):
        pass 

    @freeze_time('2024, 03, 20')
    def test_verify_rooms(self):
        # test whether the room will be updated correctly
        hotel = Hotel.objects.create(
            name='Diammond'
        )
        room_1 = Room.objects.create(
            status=Room.Status.AVAILABLE,
            hotel=hotel,
            number=1
        )

        room_2 = Room.objects.create(
            status=Room.Status.OCCUPIED,
            hotel=hotel,
            number=2
        )

        room_3 = Room.objects.create(
            status=Room.Status.OCCUPIED,
            hotel=hotel,
            number=3
        )

        room_4 = Room.objects.create(
            status=Room.Status.UNDER_MAINTENANCE,
            hotel=hotel,
            number=4
        )

        booking_1 = Booking.objects.create(
            room=room_1,
            check_in=datetime.strptime("2024-03-10", "%Y-%m-%d").date(),
            check_out=datetime.strptime("2024-03-15", "%Y-%m-%d").date()
        )

        booking_2 = Booking.objects.create(
            room=room_2,
            check_in=datetime.strptime("2024-03-10", "%Y-%m-%d").date(),
            check_out=datetime.strptime("2024-03-21", "%Y-%m-%d").date()
        )

        booking_3 = Booking.objects.create(
            room=room_3,
            check_in=datetime.strptime("2024-03-15", "%Y-%m-%d").date(),
            check_out=datetime.strptime("2024-03-19", "%Y-%m-%d").date()
        )

        booking_4 = Booking.objects.create(
            room=room_4,
            check_in=datetime.strptime("2024-03-11", "%Y-%m-%d").date(),
            check_out=datetime.strptime("2024-03-12", "%Y-%m-%d").date()
        )

        verify_rooms()
        
        room_1.refresh_from_db()
        room_2.refresh_from_db()
        room_3.refresh_from_db()
        room_4.refresh_from_db()

        self.assertEqual(
            [
                room_1.status, 
                room_2.status, 
                room_3.status, 
                room_4.status
            ],
            [
                Room.Status.AVAILABLE, 
                Room.Status.OCCUPIED,
                Room.Status.AVAILABLE,
                Room.Status.UNDER_MAINTENANCE
            ]
        )