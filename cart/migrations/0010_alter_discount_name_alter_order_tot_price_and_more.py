# Generated by Django 4.2.4 on 2023-09-11 04:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_alter_discount_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='name',
            field=models.TextField(blank=True, default=uuid.UUID('5803bed3-b04a-49a9-8d98-fd36e17cf6f6'), verbose_name='رشته تخفیف'),
        ),
        migrations.AlterField(
            model_name='order',
            name='tot_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.FloatField(verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]
