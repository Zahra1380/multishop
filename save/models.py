from django.db import models
from account.models import User
from product.models import Product

# Create your models here.
class SaveModel(models.Model):
    saver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='savers')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='save_products')
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.saver}'
