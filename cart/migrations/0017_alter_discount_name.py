# Generated by Django 4.2.4 on 2023-09-12 15:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0016_order_address_alter_discount_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='name',
            field=models.TextField(blank=True, default=uuid.UUID('2e5334a0-0560-4882-85a2-b298009dd49c'), verbose_name='رشته تخفیف'),
        ),
    ]
