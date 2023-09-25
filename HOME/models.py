from django.db import models

# Create your models here.
class CustomerServicePhone(models.Model):
    phone_number = models.CharField(max_length=20, unique=True, verbose_name='تلفن همراه')

    class Meta:
        verbose_name_plural = 'شماره ها'
        verbose_name = 'شماره'

    def __str__(self):
        return self.phone_number