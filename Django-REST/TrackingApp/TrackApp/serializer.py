from rest_framework import serializers
from .models import Clients, Orders

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ['userId', 'username', 'email_address', 'password', 'isCustomer']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['userId', 'orderId', 'description']