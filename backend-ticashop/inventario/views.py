from rest_framework import viewsets
from .models import Producto, Proveedor, MovimientoInventario
from .serializers import ProductoSerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import (
    ProductoSerializer,
    ProveedorSerializer,
    MovimientoInventarioSerializer,
)

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class MovimientoInventarioViewSet(viewsets.ModelViewSet):
    queryset = MovimientoInventario.objects.all()
    serializer_class = MovimientoInventarioSerializer

class LoginView(APIView):
    authentication_classes = []  # no exige token para loguear
    permission_classes = []

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(
                {"detail": "Credenciales inválidas"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        token, created = Token.objects.get_or_create(user=user)

        # Definimos el rol según is_staff
        role = "administrador" if user.is_staff else "operario"

        return Response({
            "token": token.key,
            "username": user.username,
            "role": role,
        })