# Generated by Django 4.2.4 on 2023-09-19 13:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0032_alter_discount_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='name',
            field=models.TextField(blank=True, default=uuid.UUID('95fd9a99-3a19-4674-bf94-44812e4e6f16'), verbose_name='رشته تخفیف'),
        ),
    ]