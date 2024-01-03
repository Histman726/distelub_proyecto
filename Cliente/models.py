from django.db import models


# Create your models here.
class Cliente(models.Model):
    id_cliente = models.IntegerField(db_column='ID_Cliente', primary_key=True)  # Field name made lowercase.
    nombre_cliente = models.CharField(db_column='Nombre_Cliente', max_length=100, blank=True,
                                      null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Dirección', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Teléfono', max_length=20, blank=True,
                                null=True)  # Field name made lowercase.

    def __str__(self):
        return self.nombre_cliente

    class Meta:
        db_table = 'clientes'


class Proveedor(models.Model):
    id_proveedor = models.IntegerField(db_column='ID_Proveedor', primary_key=True)  # Field name made lowercase.
    nombre_proveedor = models.CharField(db_column='Nombre_Proveedor', max_length=100, blank=True,
                                        null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Dirección', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Teléfono', max_length=20, blank=True,
                                null=True)  # Field name made lowercase.

    def __str__(self):
        return self.nombre_proveedor

    class Meta:
        db_table = 'proveedores'
        verbose_name_plural = "Proveedores"


class Producto(models.Model):
    id_producto = models.IntegerField(db_column='ID_Producto', primary_key=True)  # Field name made lowercase.
    nombre_producto = models.CharField(db_column='Nombre_Producto', max_length=100, blank=True,
                                       null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripción', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    categoria = models.CharField(db_column='Categoria', max_length=50, blank=True, null=True)
    imagen = models.ImageField(db_column='Imagen', upload_to='media', blank=True, null=True)
    precio_unitario = models.DecimalField(db_column='Precio_Unitario', max_digits=10, decimal_places=2, blank=True,
                                          null=True)  # Field name made lowercase.
    stock_disponible = models.IntegerField(db_column='Stock_Disponible', blank=True,
                                           null=True)  # Field name made lowercase.

    def __str__(self):
        return self.nombre_producto

    class Meta:
        db_table = 'productos'


class Venta(models.Model):
    id_venta = models.IntegerField(db_column='ID_Venta', primary_key=True)  # Field name made lowercase.
    id_cliente = models.ForeignKey(Cliente, models.CASCADE, db_column='ID_Cliente', blank=True,
                                   null=True)  # Field name made lowercase.
    fecha_venta = models.DateField(db_column='Fecha_Venta', blank=True, null=True)  # Field name made lowercase.
    total_venta = models.DecimalField(db_column='Total_Venta', max_digits=10, decimal_places=2, blank=True,
                                      null=True)  # Field name made lowercase.

    def __str__(self):
        return self.fecha_venta.strftime("%d/%m/%Y")

    class Meta:
        db_table = 'ventas'


class Compra(models.Model):
    id_compra = models.IntegerField(db_column='ID_Compra', primary_key=True)  # Field name made lowercase.
    id_proveedor = models.ForeignKey(Proveedor, models.CASCADE, db_column='ID_Proveedor', blank=True,
                                     null=True)  # Field name made lowercase.
    fecha_compra = models.DateField(db_column='Fecha_Compra', blank=True, null=True)  # Field name made lowercase.
    total_compra = models.DecimalField(db_column='Total_Compra', max_digits=10, decimal_places=2, blank=True,
                                       null=True)  # Field name made lowercase.

    def __str__(self):
        return self.fecha_compra.strftime("%d/%m/%Y")

    class Meta:
        db_table = 'compras'


class DetalleCompra(models.Model):
    id_detalle_compra = models.IntegerField(db_column='ID_Detalle_Compra',
                                            primary_key=True)  # Field name made lowercase.
    id_compra = models.ForeignKey(Compra, models.CASCADE, db_column='ID_Compra', blank=True,
                                  null=True)  # Field name made lowercase.
    id_producto = models.ForeignKey(Producto, models.CASCADE, db_column='ID_Producto', blank=True,
                                    null=True)  # Field name made lowercase.
    cantidad_comprada = models.IntegerField(db_column='Cantidad_Comprada', blank=True,
                                            null=True)  # Field name made lowercase.
    precio_compra_unitario = models.DecimalField(db_column='Precio_Compra_Unitario', max_digits=10, decimal_places=2,
                                                 blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='Subtotal', max_digits=10, decimal_places=2, blank=True,
                                   null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.id_compra.id_compra)

    class Meta:
        db_table = 'detalle_compra'


class DetalleVenta(models.Model):
    id_detalle_venta = models.IntegerField(db_column='ID_Detalle_Venta', primary_key=True)  # Field name made lowercase.
    id_venta = models.ForeignKey(Venta, models.CASCADE, db_column='ID_Venta', blank=True,
                                 null=True)  # Field name made lowercase.
    id_producto = models.ForeignKey(Producto, models.CASCADE, db_column='ID_Producto', blank=True,
                                    null=True)  # Field name made lowercase.
    cantidad_vendida = models.IntegerField(db_column='Cantidad_Vendida', blank=True,
                                           null=True)  # Field name made lowercase.
    precio_venta_unitario = models.DecimalField(db_column='Precio_Venta_Unitario', max_digits=10, decimal_places=2,
                                                blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='Subtotal', max_digits=10, decimal_places=2, blank=True,
                                   null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.id_venta.id_venta)

    class Meta:
        db_table = 'detalle_venta'
