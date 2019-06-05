from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Deparment, Province, District, Brand, Product, User, Supermarket, Chain, ChainProduct, Order, OrderDetail, Condition

admin.site.register(Deparment)
admin.site.register(Province)
admin.site.register(District)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Supermarket)
admin.site.register(Chain)
admin.site.register(ChainProduct)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Condition)
