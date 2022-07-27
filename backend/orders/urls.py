from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.orders_list, name='orders_list'),
]