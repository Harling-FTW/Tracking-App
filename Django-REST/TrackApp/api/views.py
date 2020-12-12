from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from .serializers import UserSerializer, OrderSerializer
from .models import Order
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication,)

    """@action(detail=True, methods=["POST"])
    def set_user(self, request, pk=None):"""
        


    @action(detail=True, methods=["POST"])
    def get_user(self, request, pk=None):
        user = User.objects.get(id=pk)
        response = {"Username:" : str(user.username), "Name:" : str(user.first_name) +" "+ str(user.last_name), "is_staff" : str(user.is_staff)}
        return Response(response, status = status.HTTP_200_OK)

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    
    @action(detail=True, methods=["POST"])
    def get_order(self, request, pk=None):
        order = Order.objects.get(id=pk)
        details = {"username" : str(order.username), 
        " order_id:": str(order.order_id), 
        " description:" : str(order.description),
        " weight:" : str(order.weight),
        " dispatch_date:": str(order.dispatch_date)}
        return Response(details, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=["POST"])
    def get_userhist(self,request, pk=None):
        userhist = Order.objects.filter(username_id=pk)
        details = {"order_id" : []}
        inc = 0
        for objec in userhist:
            details["order_id"].append(str(objec.order_id))
            inc+=1
        return Response(details, status = status.HTTP_200_OK)
        

    """@action(detail=True, method="POST")
    def set_order(self, request, pk=None):"""
        
