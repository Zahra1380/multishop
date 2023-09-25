from django.db import models
from product.models import Product
from account.models import User
import uuid

# Create your models here.
class Transportation(models.Model):
    title = models.CharField(max_length=20, verbose_name='عنوان')
    coast = models.FloatField(verbose_name='هزینه')
    description = models.TextField(verbose_name='توضیحات')

    class Meta:
        verbose_name = 'حمل و نقل'
        verbose_name_plural = 'حمل و نقل ها'

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order', verbose_name='کاربر')
    transport = models.ForeignKey(Transportation,  on_delete=models.CASCADE, related_name='trans', verbose_name='حمل و نقل', null=True)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    is_paid = models.BooleanField(default=False, verbose_name='وضعیت پرداخت')
    tot_price = models.FloatField(default=0)
    address = models.TextField(default='empty')

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش ها'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='item', verbose_name='سفارش')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products', verbose_name='محصول')
    size = models.CharField(max_length=12, verbose_name='اندازه')
    color = models.CharField(max_length=12, verbose_name='رنگ')
    quantity = models.SmallIntegerField(verbose_name='تعداد')
    price = models.FloatField(verbose_name='قیمت')
    total = models.FloatField(default=0)
    class Meta:
        verbose_name = 'مورد سفارشی'
        verbose_name_plural = 'موارد سفارشی'


class Discount(models.Model):
    name = models.TextField(default=uuid.uuid4(), blank=True, verbose_name='رشته تخفیف')
    percentage = models.SmallIntegerField(default=0, verbose_name='درصد تخفیف')
    quantity = models.SmallIntegerField(default=1, verbose_name='تعداد تخفیف')

    class Meta:
        verbose_name = 'تخفیف'
        verbose_name_plural = 'تخفیف ها'

    def __str__(self):
        return self.name
