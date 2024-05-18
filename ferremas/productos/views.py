from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Producto
from .serializers import ProductoSerializer

# Create your views here.

from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework.response import Response

class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


@api_view(['GET'])
def get_items(request):
    items = Producto.objects.all()
    serializer = ProductoSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_producto_detalle(request, cod_producto):
    try:
        producto = Producto.objects.get(cod_producto=cod_producto)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProductoSerializer(producto)
    return Response(serializer.data)


@api_view(['POST'])
def registrar_producto(request):
    serializer = ProductoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)