from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from core.views.user import CustomTokenObtainPairView


schema_view = get_schema_view(
   openapi.Info(
      title="Documentation API",
      default_version='v1',
      description="Booking Hotels API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="booking@api.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'api/login/', 
        CustomTokenObtainPairView.as_view(), 
        name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/', 
        TokenRefreshView.as_view(), 
        name='token_refresh'
    ),
    path(
        'swagger<format>/', 
        schema_view.without_ui(cache_timeout=0), 
        name='schema-json'
    ),
    path(
        'swagger/', 
        schema_view.with_ui('swagger', cache_timeout=0), 
        name='schema-swagger-ui'
    ),
    path(
        'redoc/', 
        schema_view.with_ui('redoc', cache_timeout=0), 
        name='schema-redoc'
    ),
    # APIs Endpoints
    path('api/', include([
        path('', include('core.urls')),
        path('', include('booking.urls'))
    ])),
]
