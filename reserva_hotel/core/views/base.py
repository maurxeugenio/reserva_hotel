from django.utils import timezone
from rest_framework import viewsets, status, filters
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated


class BaseAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_serializer_context(self):
        context = {}    
        context['user'] = self.request.user
        return context


class BaseListAPIView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []


class BaseModelViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]    

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted_at = timezone.now()
        instance.deleted_by = request.user
        instance.save()
        return Response(
            {"message": "The item has been successfully deleted"},
            status=status.HTTP_204_NO_CONTENT
        )

def get_queryset(self: APIView):
    """ Auto filter in all removed objects and company"""
    meta = self.get_serializer_class().Meta
    model = meta.model
    
    # first tries to get the ordering from the ViewModel Meta class,
    # else uses the serializer class Meta class.
    ordering_meta = hasattr(self, 'Meta') and self.Meta or meta
    
    ordering = (
        hasattr(ordering_meta, 'ordering')
        and ordering_meta.ordering
        or ['-id']
    )
    
    queryset = model.objects.filter(
        company=self.request.user.active_company,
        deleted_at=None,
    ).order_by(*ordering)
        
    return queryset


class BaseOwnedByCompanyModelViewSet(BaseModelViewSet):
    lookup_field = 'code'
    filter_backends = (
        filters.SearchFilter,
        DjangoFilterBackend,
    )
    
    def get_serializer_context(self):
        """ Adds company in context to serializer. This is default in all
        OwnedByCompany models."""
        context = super().get_serializer_context()
        if not context:
            context = {}
        context['company'] = self.request.user.active_company
        return context

    def get_queryset(self):
        return get_queryset(self)

    def get_company(self): 
        """ Returns company from context """       
        return self.get_serializer_context().get("company")


class OwnedByCompanyListAPIView(BaseListAPIView):
    def get_queryset(self):
        return get_queryset(self)