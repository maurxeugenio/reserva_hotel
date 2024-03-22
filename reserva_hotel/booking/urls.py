# rooms available of hotels
# reserve a room
# create a room
# list all rooms
# delet a room
# update a room 

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from booking.views import HotelModelViewSet, RoomModelViewSet, BookingAPIView

router = DefaultRouter()
router.register(
    r'hotels', 
    HotelModelViewSet, 
    basename='hotels'
)

router.register(
    r'rooms', 
    RoomModelViewSet, 
    basename='rooms'
)

urlpatterns = [
    path('', include(router.urls)), 
    path('bookings/', BookingAPIView.as_view(), name='bookings')
]