from django.db import models

class Rol(models.Model):
    nombreRol = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nombreRol
    

class Usuario(models.Model):
    nombreUsuario = models.CharField(max_length=50, unique=True)
    passwordHash = models.CharField(max_length=255)
    nombreCompleto = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    estado = models.CharField(max_length=20, default='ACTIVO')
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombreUsuario
    

class Proveedor(models.Model):
    rut = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150, blank=True)
    estado = models.CharField(max_length=20, default='ACTIVO')

    def __str__(self):
        return self.nombre
    

class Producto(models.Model):
    CATEGORIA_CHOICES = (
        ('ELECTRONICA', 'Electrónica'),
        ('COMPUTACION', 'Computación'),
        ('ACCESORIOS', 'Accesorios'),
        ('OTROS', 'Otros'),
    )

    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200, blank=True)
    precioUnitario = models.DecimalField(max_digits=10, decimal_places=2)
    stockActual = models.IntegerField(default=0)
    stockMinimo = models.IntegerField(default=0)
    estado = models.CharField(max_length=20, default='ACTIVO')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    categoria = models.CharField(          # 👈 NUEVO
        max_length=50,
        choices=CATEGORIA_CHOICES,
        default='OTROS',
    )

    def __str__(self):
        return self.nombre
    

class MovimientoInventario(models.Model):
    TIPO_CHOICES = (
        ('ENTRADA', 'Entrada'),
        ('SALIDA', 'Salida'),
        ('AJUSTE', 'Ajuste'),
    )

    fecha = models.DateTimeField()
    tipoMovimiento = models.CharField(max_length=20, choices=TIPO_CHOICES)
    cantidad = models.IntegerField()
    observacion = models.CharField(max_length=200, blank=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f"{self.tipoMovimiento} {self.cantidad} de {self.producto.nombre}"