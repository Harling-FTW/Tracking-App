from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UserViewSet, OrderViewSet
from rest_framework.authtoken.views import obtain_auth_token
router = routers.DefaultRouter()
router.register(r'Users', UserViewSet)
router.register(r'Orders', OrderViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', obtain_auth_token)
]