from django.db import models
from account.models import User
from product.models import Product

# Create your models here.
class DislikeModel(models.Model):
    disliker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dislikers')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='dislikes_products')
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.disliker}'
