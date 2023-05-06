from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.db.models import Count
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from . import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    list_display = ['title','unit_price','collection','inventory','inventory_status']
    list_editable = ['unit_price','inventory']
    list_per_page = 500
    search_fields = ['title']
    list_filter = ['collection','last_update']

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10 :
            return 'Low'
        return 'ok'



@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title','featured_product','porduct_count']
    search_fields = ['title']

    @admin.display(ordering='porduct_count')
    def porduct_count(self, collection):
        url =  (
            reverse('admin:store_product_changelist') 
            + '?'
            + urlencode({
                'collection__id': str(collection.id)
            }))
        return format_html('<a href="{}" >{}</a>',url,collection.porduct_count)
    

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            porduct_count = Count('product')
        )


@admin.register(models.Customer)
class CustomersAdmin(admin.ModelAdmin):
    search_fields = ['first_name','last_name']
    list_display = ['first_name','last_name','membership']
    list_editable = ['membership']
    ordering = ['first_name','last_name']
    list_per_page = 10
    search_fields = ['first_name__istartswith','last_name__istartswith']



class OrderitemInline(admin.StackedInline):
    model=  models.OrderItem
    autocomplete_fields = ['product']
    min_num = 1
    max_num = 100
    extra = 0


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    inlines =  [OrderitemInline]
    list_display = ['id','placed_at','customer']
    