from like.models import LikeModel
from django import template

register = template.Library()

@register.filter
def is_like(product):
    try:
        LikeModel.objects.get(product=product)
        return True
    except:
        return False