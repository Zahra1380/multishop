from like.models import LikeModel
from django import template

register = template.Library()

@register.filter
def has_like(user):
    try:
        LikeModel.objects.get(liker=user)
        return True
    except:
        return False