from save.models import SaveModel
from django import template

register = template.Library()

@register.filter
def is_save(product, user):
    try:
        SaveModel.objects.get(product=product, disliker=user)
        return True
    except:
        return False