from django.db import models

# Create your models here.

from django.db import models


class Deparment(models.Model):
    iddepartamento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    class Meta:
        db_table = "departamentos"

    def __str__(self):
        return self.nombre


class Province(models.Model):
    idprovincia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    iddepartamento = models.ForeignKey(Deparment, on_delete=models.CASCADE, db_column='iddepartamento')

    class Meta:
        db_table = "provincias"

    def __str__(self):
        return self.nombre

class District(models.Model):
    iddistrito = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    idprovincia = models.ForeignKey(Province, on_delete=models.CASCADE, db_column="idprovincia")

    class Meta:
        db_table = "distritos"

    def __str__(self):
        return self.nombre


class Brand(models.Model):
    idmarca = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = "marcas"

    def __str__(self):
        return self.nombre

class Product(models.Model):
    idproducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    idmarca = models.ForeignKey(Brand, on_delete=models.CASCADE, db_column="idmarca")

    class Meta:
        db_table = "productos"

    def __str__(self):
        return self.nombre

class User(models.Model):
    idusuario = models.AutoField(primary_key=True)
    apellidos = models.CharField(max_length=45)
    nombres = models.CharField(max_length=45)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=200)
    fec_registro = models.DateField(auto_now=True)
    dni = models.CharField(max_length=10, null=True, blank=True)
    distritos_iddistrito = models.ForeignKey(District, on_delete=models.CASCADE, db_column="distritos_iddistrito", null=True, blank=True)

    class Meta:
        db_table = "usuarios"

    def __str__(self):
        return self.nombres + " " + self.apellidos

class Condition(models.Model):
    idusuario = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, db_column="idusuario")
    direccionIp = models.CharField(max_length=30)
    imei = models.CharField(max_length=20)
    fechahora_registro = models.DateTimeField(auto_now=True)
    accept = models.BooleanField()

    class Meta:
        db_table = "condiciones"

    def __str__(self):
        return str(self.idusuario) + " con imei " + self.imei + " accept: " + str(self.accept)

class Supermarket(models.Model):
    idsupermercado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    ruc = models.CharField(max_length=20)

    class Meta:
        db_table = "supermercados"

    def __str__(self):
        return self.nombre

class Chain(models.Model):
    idsede = models.AutoField(primary_key=True)
    latitud = models.CharField(null=True, max_length=45, blank=True)
    longitud = models.CharField(null=True, max_length=45, blank=True)
    latitud2 = models.CharField(null=True, max_length=45, blank=True)
    longitud2 = models.CharField(null=True, max_length=45, blank=True)
    direccion = models.CharField(null=True, max_length=100, blank=True)
    iddistrito = models.ForeignKey(District, on_delete=models.CASCADE, db_column="iddistrito")
    idsupermercado = models.ForeignKey(Supermarket, on_delete=models.CASCADE, db_column="idsupermercado")

    class Meta:
        db_table = "sedes"

    def __str__(self):
        return str(self.idsupermercado) + " de " + str(self.iddistrito) + " direccion " + self.direccion

class ChainProduct(models.Model):
    idproductosede = models.AutoField(primary_key=True)
    idproducto = models.ForeignKey(Product, on_delete=models.PROTECT, db_column="idproducto")
    idsede = models.ForeignKey(Chain, on_delete=models.CASCADE, db_column="idsede")
    precio = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        db_table = "productos_sedes"

    def __str__(self):
        return str(self.idproducto) + " S/. " + str(self.precio) + " en " + str(self.idsede)

class Order(models.Model):
    idpedido = models.AutoField(primary_key=True)
    fec_pedido = models.DateField(auto_now=True)
    usuarios_idusuario = models.ForeignKey(User, on_delete=models.CASCADE, db_column="usuarios_idusuario")
    sedes_idsede = models.ForeignKey(Chain, on_delete=models.CASCADE, db_column="sedes_idsede")

    class Meta:
        db_table = "pedidos"

    def __str__(self):
        return str(self.usuarios_idusuario) + " con pedido fecha " + str(self.fec_pedido)

class OrderDetail(models.Model):
    idpedidodeta = models.AutoField(primary_key=True)
    idpedido = models.ForeignKey(Order, on_delete=models.CASCADE, db_column="idpedido")
    idproducto = models.ForeignKey(Product, on_delete=models.CASCADE, db_column="idproducto")
    cantidad = models.IntegerField()
    precioxunidad = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        managed = False
        db_table = "pedidosdeta"



    def __str__(self):
        return str(self.idpedido) + " pidió " + str(self.cantidad) + " " + str(self.idproducto)


