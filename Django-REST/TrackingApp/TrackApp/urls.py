from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from .views import OrderList, ClientList, OrderDetail, ClientDetail

urlpatterns = [
    path('api/Orders/', OrderList.as_view()),
    path('api/Clients/', ClientList.as_view()),
    path('api/Orders/<int:pk>', OrderDetail.as_view()),
    path('api/Clients/<int:pk>', ClientDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)