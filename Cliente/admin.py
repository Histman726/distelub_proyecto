from django.contrib import admin
from Cliente.models import *

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(DetalleCompra)
admin.site.register(Compra)
