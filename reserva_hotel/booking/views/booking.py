from core.views import BaseAPIView
from booking.serializers import (
    BookingCreateSerializer, BookingDetailSerializer
)
from rest_framework.response import Response
from rest_framework import status
from booking.models import Booking


class BookingAPIView(BaseAPIView):
    def post(self, request):
        context = self.get_serializer_context()

        serializer = BookingCreateSerializer(
            data=request.data, 
            context=context
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def get(self, request):
        queryset = Booking.objects.filter(user=self.request.user)

        serializer_class = BookingDetailSerializer(
            queryset, many=True
        )
        
        return Response(
            serializer_class.data,
            status=status.HTTP_200_OK
        )
