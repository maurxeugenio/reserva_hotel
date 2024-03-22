from core.views.base import BaseOwnedByCompanyModelViewSet
from booking.serializers import (
    HotelDetailSerializer, HotelCreateSerializer
)
from rest_framework.permissions import IsAuthenticated
from booking.permissions import IsOwnerOrEmployee



class HotelModelViewSet(BaseOwnedByCompanyModelViewSet):

    def get_serializer_class(self):
        if self.action == 'create':
            return HotelCreateSerializer

        return HotelDetailSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes.append(IsOwnerOrEmployee)

        return [permission() for permission in permission_classes]
