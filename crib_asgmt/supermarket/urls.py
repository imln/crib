from django.urls import path, include
from rest_framework.routers import DefaultRouter
from supermarket.views import ProductList


urlpatterns = [
    path('items/', ProductList.as_view(), name='items'),
]