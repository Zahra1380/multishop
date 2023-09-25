from save.models import SaveModel
from django import template

register = template.Library()

@register.filter
def has_save(user):
        return SaveModel.objects.filter(saver=user)