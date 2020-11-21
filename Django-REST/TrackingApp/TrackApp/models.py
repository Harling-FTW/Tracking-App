from django.db import models

# Create your models here.
class Clients(models.Model):
    userId = models.IntegerField(null = False, blank = False, unique = True)
    username = models.CharField(max_length = 20, null = False, blank = False)
    email_address = models.CharField(max_length = 36, null = False, blank = False)
    password = models.CharField(max_length = 16, null = False, blank = False)
    isCustomer = models.BooleanField(default=True)
     
class Orders(models.Model):
    userId = models.IntegerField(null = False, blank = False)
    orderId = models.IntegerField(null = False, blank = False, unique = True)
    description = models.TextField(max_length = 123,)
