# Generated by Django 4.2.4 on 2023-09-17 07:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0022_alter_discount_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='name',
            field=models.TextField(blank=True, default=uuid.UUID('8027819c-f729-47fb-9dd6-93265723e7f3'), verbose_name='رشته تخفیف'),
        ),
    ]