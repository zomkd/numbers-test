from django.urls import path

from . import views

urlpatterns = [
    path('orders/', views.orders_list, name='orders_list'),
]