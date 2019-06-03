from rest_framework import serializers
from .models import Deparment, Chain, Product, Brand, ChainProduct, Province, User, District, Order, Supermarket, DetailOrder
import datetime
from django.contrib.auth.hashers import make_password

class DepartmentSerializar(serializers.Serializer):
    iddepartamento = serializers.IntegerField(required=False)
    nombre = serializers.CharField(max_length=45)

    def create(self, validated_data):
        return Deparment.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.save()
        return instance


class ProvinceSerializer(serializers.Serializer):
    idprovincia = serializers.IntegerField(required=False)
    nombre = serializers.CharField(max_length=45)
    iddepartamento = serializers.PrimaryKeyRelatedField(queryset=Deparment.objects.all())

    def create(self, validate_data):
        return Province.objects.create(**validate_data)

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.iddepartamento = validated_data.get('iddepartamento', instance.iddepartamento)
        instance.save()
        return instance

    class Meta:
        model = Province
        fields = '__all__'


class DistrictSerializar(serializers.Serializer):
    iddistrito = serializers.IntegerField(required=False)
    nombre = serializers.CharField(max_length=60)
    idprovincia = serializers.PrimaryKeyRelatedField(queryset=Province.objects.all())

    def create(self, validated_data):
        return District.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.idprovincia = validated_data.get('idprovincia', instance.idprovincia)
        instance.save()
        return instance



class ProductSerializer(serializers.Serializer):
    idproducto = serializers.IntegerField()
    nombre = serializers.CharField(max_length=45)
    idmarca = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())

    class Meta:
        model = Product
        fields = '__all__'


class ChainProductoSerializer(serializers.Serializer):
    idproductosede = serializers.IntegerField()
    precio = serializers.DecimalField(max_digits=19, decimal_places=2)
    idproducto = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    idsede = serializers.PrimaryKeyRelatedField(queryset=Chain.objects.all())



    class Meta:
        model = ChainProduct
        fields = '__all__'

class UserSerializer(serializers.Serializer):
    idusuario = serializers.IntegerField(required=False)
    apellidos = serializers.CharField(max_length=45)
    nombres = serializers.CharField(max_length=45)
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=200)
    fec_registro = serializers.DateField(required=False)
    dni = serializers.CharField(max_length=10, required=False)
    distritos_iddistrito = serializers.PrimaryKeyRelatedField(queryset=District.objects.all(), required=False)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])

        return User.objects.create(**validated_data)



