from dislike.models import DislikeModel
from django import template

register = template.Library()

@register.filter
def is_dislike(product, user):
    try:
        DislikeModel.objects.get(product=product, disliker=user)
        return True
    except:
        return False