from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response

from .serializers import CategorySerializer
from .models import Category

class CategoryList(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
