from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='home'),
    path('fashion/', views.fashion,name='fashion'),
    path('product/', views.product_list,name='product'),
    path('product/<int:pk>/', views.product_detail,name='product-detail'),
    path('collection/', views.collection_list,name='collection'),
    path('collection/<int:pk>/', views.collection_detail,name='collection-detail'),
]