from like.models import LikeModel
from django import template

register = template.Library()

@register.filter
def is_like(product, user):
    try:
        LikeModel.objects.get(product=product, liker=user)
        return True
    except:
        return False
