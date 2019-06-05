from django.shortcuts import render

# Create your views here.


from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_401_UNAUTHORIZED
)


import numpy as np
import datetime
from tensorflow import keras
from keras.preprocessing.image import load_img, img_to_array


from rest_framework import viewsets
from .models import Deparment, Province, ChainProduct, Product, User, Order, OrderDetail, Condition
from .serializers import DepartmentSerializar, ProvinceSerializer, ChainProductoSerializer, ProductSerializer, UserSerializer, OrderDetailSerializer, OrderSerializer, ConditionSerializer
from rest_framework.views import APIView, Response
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password, check_password

class CustomView(APIView):
    def get(self, request, format=None):

        return Response("Some Get Response")

    def post(self, request, format=None):
        return Response("Some Post Response")

class AuthenticateViewSet(APIView):

    def post(self, request):
        if request.method == 'POST':
            email = request.data.get("email")
            password = request.data.get("password")
            if email is None or password is None:
                return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)

            try:
                user = User.objects.get(email=email)
                check_pass = check_password(password, user.password)

                if check_pass is False:
                    return Response({'error': 'Invalid Credentials'}, status=HTTP_401_UNAUTHORIZED)

            except ObjectDoesNotExist:
                return Response({'error': 'Invalid Credentials'}, status=HTTP_401_UNAUTHORIZED)



            user_serialized = UserSerializer(user, many=False).data

            return Response(user_serialized, status=HTTP_200_OK)





class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RecognitionProduct(APIView):
    serializer_class = ChainProductoSerializer

    def post(self, request):
        if request.method == "POST":
            file = request.FILES['file']
            id_producto = self.predict(file)
            id_sede = request.POST['id_sede']

            producto = ChainProduct.objects.get(idproducto=id_producto, idsede=id_sede)

            chainproduct_serialized = ChainProductoSerializer(producto, many=False).data
            return Response(chainproduct_serialized)


    def predict(self, file):
        longitud, altura = 100, 100
        modelo = './api/modelos/modelo.h5'
        pesos_modelo = './api/modelos/pesos.h5'
        cnn = keras.models.load_model(modelo)
        cnn.load_weights(pesos_modelo)

        x = load_img(file, target_size=(longitud, altura))
        x = img_to_array(x)
        x = np.expand_dims(x, axis=0)
        array = cnn.predict(x)
        result = array[0]
        answer = np.argmax(result)

        id_product = answer+1



        return id_product


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Deparment.objects.all()
    serializer_class = DepartmentSerializar


class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer

class ConditionViewSet(viewsets.ModelViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer


