from django.contrib import admin
from .models import Product, Review, Order, OrderItem, ShippingAddress, New

# Register your models here.

admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(New)
