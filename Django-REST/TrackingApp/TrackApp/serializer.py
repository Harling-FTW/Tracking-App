from rest_framework import serializers
from .models import Clients, Orders
from django.contrib.auth.models import User

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ['userId', 'username', 'email_address', 'password', 'isCustomer']

class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Orders
        fields = ['userId', 'orderId', 'description', 'owner']
        

class UserSerializer(serializers.ModelSerializer):
    orders = serializers.PrimaryKeyRelatedField(many=True, queryset=Orders.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'orders']