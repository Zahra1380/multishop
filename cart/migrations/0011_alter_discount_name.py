# Generated by Django 4.2.4 on 2023-09-11 04:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_alter_discount_name_alter_order_tot_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='name',
            field=models.TextField(blank=True, default=uuid.UUID('49fa7f2c-e379-4477-8182-f45446710996'), verbose_name='رشته تخفیف'),
        ),
    ]
