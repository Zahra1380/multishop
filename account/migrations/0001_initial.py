# Generated by Django 4.2.4 on 2023-09-10 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='آدرس ایمیل')),
                ('phone_number', models.CharField(max_length=20, unique=True, verbose_name='تلفن همراه')),
                ('full_name', models.CharField(max_length=50, null=True, verbose_name='نام کامل')),
                ('is_active', models.BooleanField(default=True, verbose_name='اکتیو بودن کاربر')),
                ('is_admin', models.BooleanField(default=False, verbose_name='ادمین بودن کاربر')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربرها',
            },
        ),
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=11, verbose_name='تلفن')),
                ('code', models.SmallIntegerField(verbose_name='کد')),
                ('expration_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انقضا')),
            ],
            options={
                'verbose_name': 'پیامک ارسالی',
                'verbose_name_plural': 'پیامک های ارسالی',
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='نام')),
                ('last_name', models.CharField(max_length=255, verbose_name='نام خانوادگی')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='ایمیل')),
                ('phone', models.CharField(max_length=11, verbose_name='شماره تماس')),
                ('address', models.CharField(max_length=300, verbose_name='آدرس')),
                ('zip_code', models.CharField(max_length=30, verbose_name='کد پستی')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresess', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'آدرس',
                'verbose_name_plural': 'آدرس ها',
            },
        ),
    ]