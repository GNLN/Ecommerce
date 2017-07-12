from django.contrib import admin
#import autocomplete_light
from .models import Product, return_order, Inventory,Category, Order, Payment, Track

# Register your models here.
#class return_orderAdmin(admin.ModelAdmin):

admin.site.register(Product)
admin.site.register(return_order)
admin.site.register(Inventory)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Track)
