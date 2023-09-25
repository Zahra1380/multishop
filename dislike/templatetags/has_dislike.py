from dislike.models import DislikeModel
from django import template

register = template.Library()

@register.filter
def has_dislike(user):
    return DislikeModel.objects.filter(disliker=user)
