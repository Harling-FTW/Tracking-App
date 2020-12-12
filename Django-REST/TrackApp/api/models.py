from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Order(models.Model):
    order_id = models.IntegerField(null=False, blank=False, validators=(MinValueValidator(1),), unique=True)
    username = models.ForeignKey(User, null = True, on_delete=models.CASCADE)
    description = models.CharField(max_length=132, blank=True, null=False)
    weight = models.DecimalField(max_digits= 5, decimal_places=2)
    order_date = models.DateField(null=False, blank=False)
    dispatch_date = models.DateField(null=False, blank=True)
    received_date = models.DateField(null=True, blank=True)
    latest_location = models.CharField(default = "Beijing, Chinal",max_length=32)

