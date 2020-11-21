from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializer import ClientSerializer, OrderSerializer
from .models import Clients, Orders
# Create your views here.

def sumFeed(request):
    return HttpResponse("Oi")

class Clientviewset(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Clients.objects.all()
    
class Orderviewset(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Orders.objects.all()


