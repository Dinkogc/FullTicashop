from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginView, ProductoViewSet, ProveedorViewSet, MovimientoInventarioViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet, basename='producto')
router.register(r'proveedores', ProveedorViewSet, basename='proveedor')
router.register(r'movimientos', MovimientoInventarioViewSet, basename='movimiento')

urlpatterns = [
    path('login/', LoginView.as_view(), name='api-login'),
    path('', include(router.urls)),
]