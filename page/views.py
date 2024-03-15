from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Product, Material, ProductMaterial, Warehouses
from .serializers import ProductSerializer, MaterialSerializer, WarehousesSerializer, ProductMaterialSerializer

from rest_framework.views import APIView


class ProductAPIList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({'result': serializer.data})


class MaterialList(generics.ListAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class WarehousesList(generics.ListAPIView):
    queryset = Warehouses.objects.all()
    serializer_class = WarehousesSerializer


class ProductMaterialList(generics.ListAPIView):
    queryset = ProductMaterial.objects.all()
    serializer_class = ProductMaterialSerializer
