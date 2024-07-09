from rest_framework import mixins
from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.


# CUSTOMER - LIST AND DETAILS --------------------------------------------------------------------------------->

class CustomerList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



# PRODUCT - LIST AND DETAILS --------------------------------------------------------------------------------->

class ProductList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



# CATEGORY - LIST AND DETAILS --------------------------------------------------------------------------------->

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



# ORDER - LISTS AND DETAILS --------------------------------------------------------------------------------->

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer