# Generated by Django 4.2.4 on 2023-09-21 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0019_product_dislikes_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='بدنه')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='product.comment', verbose_name='والد')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_product', to='product.product', verbose_name='کالا')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'کامنت',
                'verbose_name_plural': 'کامنت ها',
            },
        ),
    ]
