from decimal import Decimal
from rest_framework import serializers
from .models import *

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id','title','products_count']

    products_count = serializers.IntegerField(read_only = True)

    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length = 255)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','description','slug','inventory','unit_price','price_with_tax','collection']


    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    def calculate_tax(self, product:Product):
        return product.unit_price * Decimal(1.1)

    # to view the fields invidualy(old mathod)-->
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=6,decimal_places=2,source = 'unit_price')


    # to change or customise validate module -->> 
    # def validate(self, data):
    #     if data['password'] != data['confirm_password']:
    #         return serializers.ValidationError('Password do not match')
    #     else:
    #         return data


    # to show Collection as a hyperlink-->
    # collection = serializers.HyperlinkedRelatedField(
    #     queryset = Collection.objects.all(),
    #     view_name= 'collection-detail'
    # )


    # To view the field as a nested object -->
    # collection = CollectionSerializer()

    # if you want to show the Number representation of this field--->
    # collection = serializers.PrimaryKeyRelatedField(
    #     queryset = Collection.objects.all()
    # )


    # if you want to show the string representation of this field --->
    # collection = serializers.StringRelatedField()



    
    


