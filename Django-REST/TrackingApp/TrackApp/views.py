from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status, permissions
from .serializer import ClientSerializer, OrderSerializer, UserSerializer
from .models import Clients, Orders
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
# Create your views here.


class OrderList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get(self, request, format=None):
        orders = Orders.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get(self, request, format=None):
        clients = Clients.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get_object(self, pk):
        try:
            return Orders.objects.get(pk=pk)
        except Orders.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        orders = self.get_object(pk)
        serializer = OrderSerializer(orders)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        orders = self.get_object(pk)
        serializer = OrderSerializer(orders, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ClientDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get_object(self, pk):
        try:
            return Clients.objects.get(pk=pk)
        except Clients.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        clients = self.get_object(pk)
        serializer = ClientSerializer(clients)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        clients = self.get_object(pk)
        serializer = ClientSerializer(clients, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        client = self.get_object(pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer