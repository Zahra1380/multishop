from like.models import LikeModel
from django import template

register = template.Library()

@register.filter
def has_like(user):
    return LikeModel.objects.filter(liker=user)