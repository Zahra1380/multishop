from cart.models import Order
from django import template

register = template.Library()

@register.filter
def has_order(user):
    return Order.objects.filter(user=user, is_paid=False)
