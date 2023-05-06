from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *
# Create your views here.

def index(request):
    return render(request,'index.html',{})

def fashion(request):
    return render(request,'fashion.html',{})

@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        queryset = Product.objects.select_related('collection').all()
        serializer = ProductSerializer(
            queryset,
            many = True,
            context={'request': request}
            )
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    

@api_view(['GET','PUT','DELETE'])
def product_detail(request,pk):
    product = get_object_or_404(Product,pk=pk)
    if request.method == 'GET':
        serializer = ProductSerializer(product,context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        if product.orderitem_set.count()>0:
            return Response({'Message':'You can\'t delete the Product'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            product.delete()
            return Response({'Message':'Product Is deleted'},status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def collection_list(request):
    if request.method == 'GET':
        queryset = Collection.objects.annotate(products_count = Count('product')).all()
        serializer = CollectionSerializer(
            queryset,
            many = True,
            context={'request': request}
            )
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)



@api_view(['GET','PUT','DELETE'])
def collection_detail(request,pk):
    collection = get_object_or_404(
        Collection.objects.annotate(
        products_count = Count('product')
        ),pk=pk)
    if request.method == 'GET':
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CollectionSerializer(collection,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        collection.delete()
        return Response({'Message':'Product Is deleted'},status=status.HTTP_204_NO_CONTENT)
    