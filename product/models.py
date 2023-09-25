from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.utils.text import slugify
from account.models import User
from django.urls import reverse


class Gender(models.Model):
    # men, women, kids
    image = models.ImageField(upload_to='gender', default='gender/20230508_193336_FLAFkZA.jpg')
    gender = models.CharField(max_length=5, verbose_name='جنسیت')
    explain = models.TextField(default='')

    class Meta:
        verbose_name = 'جنسیت'
        verbose_name_plural = 'جنسیت ها'

    def __str__(self):
        return self.gender


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subs_category', blank=True, null=True,
                               verbose_name='والد')
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = models.SlugField(verbose_name='سلاگ')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class ProductSize(models.Model):
    title = models.CharField(max_length=30, verbose_name='اندازه')

    class Meta:
        verbose_name = 'اندازه'
        verbose_name_plural = 'اندازه ها'

    def __str__(self):
        return self.title


class ProductColor(models.Model):
    color = models.CharField(max_length=30, verbose_name='رنگ')

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = 'رنگ'
        verbose_name_plural = 'رنگ ها'


# Create your models here.
class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='products')
    title = models.CharField(max_length=30, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    price = models.FloatField(verbose_name='قیمت')
    quantity = models.PositiveIntegerField(default=0, verbose_name='تعداد')
    size = models.ManyToManyField(ProductSize, related_name='product_size', null=True, blank=True,
                                  verbose_name='اندازه')
    color = models.ManyToManyField(ProductColor, related_name='product_color', null=True, blank=True,
                                   verbose_name='رنگ')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)
    gender = models.ForeignKey(Gender, related_name='genders', null=True, on_delete=models.CASCADE,
                               verbose_name='جنسیت')
    simular_product = models.ManyToManyField('self', related_name='simular_product', null=True, blank=True)

    is_special = models.BooleanField(default=False)

    likes_count = models.IntegerField(default=0)
    dislikes_count = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def get_absolute_url(self):
        return reverse('Product:product-detail', args=[self.slug])

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save()

class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image_product', verbose_name='کالا')
    image = models.ImageField(upload_to='products', verbose_name='عکس')


class ProductInformation(models.Model):
    text = models.TextField(verbose_name='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='information', verbose_name='')

    class Meta:
        verbose_name = 'اطلاع محصول'
        verbose_name_plural = 'اطلاعات محصول'

    def __str__(self):
        return self.text[:10]


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comment_product', verbose_name='کالا')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user', verbose_name='کاربر')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='reply',
                               verbose_name='والد')
    body = models.TextField(verbose_name='بدنه')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return self.body[:50]

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'
