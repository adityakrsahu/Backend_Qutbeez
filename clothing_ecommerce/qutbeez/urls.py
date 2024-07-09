from django.urls import path
from .views import *

urlpatterns = [
    path('CustomerList/', CustomerList.as_view(), name="CustomerList"),
    path('CustomerDetail/<int:pk>/', CustomerDetail.as_view(), name="CustomerDetail"),
]
