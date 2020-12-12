from rest_framework import serializers
from .models import Order
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","first_name", "last_name", "username", "is_staff"]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id', 'username', 'description', 'weight', 'order_date', 'dispatch_date', 'latest_location']