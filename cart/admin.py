from django.contrib import admin
from .models import Order, OrderItem, Transportation, Discount


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem


@admin.register(Transportation)
class TransportationAdmin(admin.ModelAdmin):
    list_display = ['title', 'coast']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_paid')
    inlines = [OrderItemAdmin]
    list_filter = ['is_paid']


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage', 'quantity')
    list_filter = ['quantity']
