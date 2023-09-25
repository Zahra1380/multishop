from django import template
from product.models import Product
from like.models import LikeModel
from dislike.models import DislikeModel
register = template.Library()


@register.filter
def get_list(dictionary, key):
    return dictionary.getlist(key)


@register.filter
def is_exsist(lst, val):
    return str(val) in lst


def like_dislike(product):
    product.likes_count = LikeModel.objects.filter(product=product).count()
    product.dislikes_count = DislikeModel.objects.filter(product=product).count()
    product.save()

@register.filter
def most_popular_product(products):
    for product in products:
        like_dislike(product)
    return Product.objects.all().order_by('-likes_count').filter(likes_count__gt=0)[:10]

@register.filter
def prcent(val, mul):
    return val * mul /100
