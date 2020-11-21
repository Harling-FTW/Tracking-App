from django.urls import path, include
from . import views
from rest_framework import routers
from .views import Clientviewset, Orderviewset

router = routers.DefaultRouter()
router.register('/Clients', Clientviewset)
router.register('/Orders', Orderviewset)
urlpatterns = [
    path('', views.sumFeed),
    path('pizza', include(router.urls)),
]
