from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='home'),
    path('fashion/', views.fashion,name='fashion'),
    path('product/', views.ProductList.as_view(),name='product'),
    path('product/<int:pk>/', views.ProductDetail.as_view(),name='product-detail'),
    path('collection/', views.CollectionList.as_view(),name='collection'),
    path('collection/<int:pk>/', views.CollectionDetail.as_view(),name='collection-detail')
]