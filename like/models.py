from django.db import models
from account.models import User
from product.models import Product

# Create your models here.
class LikeModel(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likers')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='like_products')
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.liker}'