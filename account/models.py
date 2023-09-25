from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="آدرس ایمیل",
        max_length=255,
        unique=True,
        null=True,
        blank=True,
    )
    phone_number = models.CharField(max_length=20, unique=True, verbose_name='تلفن همراه')
    full_name = models.CharField(max_length=50, null=True, verbose_name='نام کامل')
    is_active = models.BooleanField(default=True, verbose_name='اکتیو بودن کاربر')
    is_admin = models.BooleanField(default=False, verbose_name='ادمین بودن کاربر')
    image = models.ImageField(upload_to='user', default='user/img.png')
    objects = UserManager()
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ['email', 'full_name']

    class Meta:
        verbose_name_plural = 'کاربرها'
        verbose_name = 'کاربر'
    def __str__(self):
        return self.phone_number

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog:blog_detail', args=[self.email])
class OTP(models.Model):
    token = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=11, verbose_name='تلفن')
    code = models.SmallIntegerField(verbose_name='کد')
    expration_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انقضا')
    class Meta:
        verbose_name='پیامک ارسالی'
        verbose_name_plural='پیامک های ارسالی'

    def __str__(self):
        return self.phone

class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='addresess', verbose_name='کاربر')
    first_name = models.CharField(max_length=255, verbose_name='نام')
    last_name = models.CharField(max_length=255, verbose_name='نام خانوادگی')
    email = models.EmailField(blank= True, null=True, verbose_name='ایمیل')
    phone = models.CharField(max_length=11, verbose_name='شماره تماس')
    address = models.CharField(max_length=300, verbose_name='آدرس')
    zip_code = models.CharField(max_length=30, verbose_name='کد پستی')

    class Meta:
        verbose_name = 'آدرس'
        verbose_name_plural = 'آدرس ها'

    def __str__(self):
        return self.phone

class CustomerService(models.Model):
    phone = models.CharField(max_length=11, verbose_name='شماره خدمات')
    address = models.TextField(null=True,  verbose_name='آدرس')
    site_email = models.EmailField(null=True,  verbose_name='ایمیل پشتیبانی')

    class Meta:
        verbose_name = 'شماره'
        verbose_name_plural = 'شماره ها'


    def __str__(self):
        return self.phone