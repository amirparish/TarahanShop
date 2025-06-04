from django.urls import path
from . import views

urlpatterns = [
    #custom catalog urls
    path('', views.product_list, name='product_list'),
]