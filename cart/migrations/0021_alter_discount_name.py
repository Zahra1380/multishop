# Generated by Django 4.2.4 on 2023-09-13 13:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0020_alter_discount_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='name',
            field=models.TextField(blank=True, default=uuid.UUID('931cbc8a-ef53-4f2f-8c9f-e1a23ab1ccbe'), verbose_name='رشته تخفیف'),
        ),
    ]
