from django.shortcuts import render
from supermarket.serializers import ProductSerializer
from .models import Category, Product
from rest_framework import generics


class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        
        # filter using category
        category = self.request.query_params.get('category')
        if category is not None:
            queryset = queryset.filter(subcategory__category__name=category)
        
        # filter using subcategory
        subcategory = self.request.query_params.get('subcategory')
        if subcategory is not None:
            queryset = queryset.filter(subcategory__name=subcategory)

        # filter using name
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)

        # return final queryset
        return queryset