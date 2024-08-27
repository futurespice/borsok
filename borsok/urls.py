from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Настройка Swagger для документации API
schema_view = get_schema_view(
    openapi.Info(
        title="Borsok API",
        default_version='v1',
        description="API документация для Borsok проекта",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('menu.urls')),
    path('api/', include('promotions.urls')),
    path('api/', include('cart.urls')),
    path('api/', include('promocodes.urls')),
    path('api/', include('users.urls')),
    path('api/', include('orders.urls')),

]
