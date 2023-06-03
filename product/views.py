from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


""" Getting products by category id """
class ProductCategoryList(APIView):
    def get(self, request, pk, format=None):
        products = Product.objects.filter(category_id = pk)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
