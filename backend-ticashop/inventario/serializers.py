from rest_framework import serializers
from .models import Producto, Proveedor, MovimientoInventario

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = "__all__"


class MovimientoInventarioSerializer(serializers.ModelSerializer):
    
    precioUnitario = serializers.DecimalField(
        source="producto.precioUnitario",
        max_digits=10,
        decimal_places=2,
        read_only=True,
    )
    total = serializers.SerializerMethodField()
    productoNombre = serializers.CharField(
        source="producto.nombre", read_only=True
    )
    proveedorNombre = serializers.CharField(
        source="producto.proveedor.nombre", read_only=True
    )

    class Meta:
        model = MovimientoInventario
        fields = [
            "id",
            "producto",         
            "productoNombre",   
            "proveedorNombre",  
            "cantidad",
            "precioUnitario",  
            "total",            
            "observacion",
            "fecha",
            "tipoMovimiento",
            "usuario",
        ]

    def get_total(self, obj):
        precio = obj.producto.precioUnitario
        if precio is not None:
            return obj.cantidad * precio
        return None