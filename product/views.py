from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductCategoryList(APIView):
    """ Getting products by category id """

    def get(self, request, pk, format=None):
        datas = []
        products = Product.objects.filter(category_id=pk)

        for x in products:
            data = {
                "id": x.id,
                "name": x.name,
                "price": x.price,
                "ready_time": x.ready_time,
                "img": x.image_url,
            }
            datas.append(data)

        return Response(datas)


class ProductDescription(APIView):
    """ Getting product description """

    def get(self, request, pk, format=None):
        product = Product.objects.get(id=pk)
        data = {
            "id": product.id,
            "description": product.description
        }
        
        return Response(data)
